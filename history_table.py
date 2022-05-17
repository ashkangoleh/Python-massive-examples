import os
from datetime import datetime
import psycopg2 as pg
import logging
import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
from calendar import timegm
from datetime import timedelta, datetime, timezone, time
import pytz
from typing import Union, List


def history_model(db_connect, now: datetime, cols: list, agg_funcs: list, resolution: str) -> pd.DataFrame:
    # Last modified: 23-Bahman
    indexes = {
        '15min': pd.Timedelta("14 min 59 sec"),
        '1H': pd.Timedelta("59 min 59 sec"),
        '1D': pd.Timedelta("23 hour 59 min 59 sec")
    }
    if resolution == '15min':
        start_time, end_time = update_15M(now)
    elif resolution == '1H':
        start_time, end_time = update_1H(now)
    elif resolution == '1D':
        start_time, end_time = update_1D(now)
    # print(start_time, end_time)
    start_time = utcdatetime2timestamp(start_time)
    end_time = utcdatetime2timestamp(end_time)

    chunk_df = sequential_modeler(
        db_connect, start_time=start_time, end_time=end_time)
    # print(chunk_df)
    aggs = named_aggs(cols, agg_funcs)
    # print(resolution)
    df = temporal_granularity(chunk_df, aggs, resolution)
    df.index = df.index + indexes[resolution]

    return df


def utcdatetime2timestamp(utc: datetime) -> int:
    return timegm(utc.timetuple())


def named_aggs(cols: list, agg_funcs: list) -> dict:
    aggregations = {}
    for col in cols:
        aggregations[col] = agg_funcs
    return aggregations


def temporal_granularity(df: pd.DataFrame, aggregations: dict, resolutions: Union[List[str], str]) -> Union[
        pd.DataFrame, dict]:
    if isinstance(resolutions, list):
        return_values: Dict[str, Any] = {}
        for resolution in resolutions:
            return_values[resolution] = df.resample(
                resolution).agg(aggregations)
        return return_values
    elif isinstance(resolutions, str):
        return df.resample(resolutions).agg(aggregations)


def sequential_modeler(db_connect, start_time, end_time):
    query = """
        SELECT * FROM block_stats
        WHERE time BETWEEN {0} AND {1}
    """.format(start_time, end_time)

    chunk_df = streaming_to_df(
        query, db_connect, streaming=True, chunk_size=1024 * 10)

    if chunk_df.empty:
        chunk_df = pd.DataFrame(index=[pd.to_datetime(
            end_time, utc=pytz.utc, unit='s')], columns=chunk_df.columns)
    else:
        chunk_df.index = pd.to_datetime(chunk_df.time, utc=pytz.utc, unit='s')
        chunk_df.sort_index(inplace=True)

    chunk_df.drop(columns=['time'])

    return chunk_df


def streaming_from_postgres(query, sqlalchemy_db_url, chunk_size: int = 1000):

    engine = create_engine(sqlalchemy_db_url)
    # With `stream_results=True` we can process
    conn = engine.connect().execution_options(stream_results=True)
    # arbitrarily large SQL results as a series of DataFrames without running out of memory.
    # Read more at https://pythonspeed.com/articles/pandas-sql-chunking/

    return conn


def streaming_to_df(query, db_connect, streaming: bool = False, chunk_size: int = 1024) -> pd.DataFrame:

    con_str = "host={host} user={user} dbname={dbname} password={password} port={port}".format(
        **db_connect)
    sqlalchemy_db_url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        **db_connect)
    # sqlalchemy_db_url = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{dbname}".format(**db_connect)
    stream_conn = streaming_from_postgres(query, sqlalchemy_db_url, chunk_size)

    li = []
    if streaming:
        for chunk_df in tqdm(pd.read_sql(query, con=stream_conn, chunksize=chunk_size)):
            li.append(chunk_df)

    df = pd.concat(li, axis=0)
    return df


def floor_date(date, **kwargs):
    """
    Last Modified: 2 Bahman 1400

    """
    secs = timedelta(**kwargs).total_seconds()
    return datetime.fromtimestamp(date.timestamp() - date.timestamp() % secs, tz=pytz.utc)


def update_15M(time_now):
    end_time = floor_date(time_now, minutes=15) - timedelta(seconds=1)
    start_time = floor_date(time_now, minutes=15) - timedelta(minutes=15)
    return start_time, end_time


def update_1H(time_now):
    # end_time = pd.Timestamp(time_now).floor('60min').to_pydatetime() - timedelta(seconds=1)
    end_time = pd.Timestamp(time_now).floor('60min') - timedelta(seconds=1)
    # start_time = pd.Timestamp(time_now).floor('60min').to_pydatetime() - timedelta(hours=1)
    start_time = pd.Timestamp(time_now).floor('60min') - timedelta(hours=1)
    return start_time, end_time


def update_1D(time_now):
    # end_time = pd.Timestamp(time_now).floor('60min').to_pydatetime() - timedelta(seconds=1)
    end_time = pd.Timestamp(time_now).floor('1D') - timedelta(seconds=1)
    # start_time = pd.Timestamp(time_now).floor('60min').to_pydatetime() - timedelta(hours=1)
    start_time = pd.Timestamp(time_now).floor('1D') - timedelta(days=1)
    return start_time, end_time


if __name__ == '__main__':
    db_connect = dict(host='venus.arz.team',
                      dbname='blocks',
                      port='5434',
                      user='sync_blocks',
                      password='ec911cb9d76445c3bfdef2c2b3c33941')
    con_str = "host={host} user={user} dbname={dbname} password={password} port={port}".format(
        **db_connect)

    query = """
        SELECT * FROM block_stats
        ORDER BY id DESC 
    """
    now = datetime(2022, 1, 6, 15, 17, tzinfo=pytz.utc)
    cols = ['totalfee', 'total_size']
    agg_funcs = ["sum", "count"]
    resolution = '1H'
    next_index = {
        '15min': pd.Timedelta("15 min 5 sec"),
        '1H': pd.Timedelta("1 hour 5 min"),
        '1D': pd.Timedelta("1 day 5 hour")
    }
    # TypeError: can't compare offset-naive and offset-aware datetimes
    while datetime.now(tz=pytz.utc) > now:
        df = history_model(db_connect, now, cols, agg_funcs, resolution)
        print(df)
        now = df.index[-1] + next_index[resolution]
