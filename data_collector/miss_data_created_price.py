import numpy as np
import pandas as pd
import pytz
from sqlalchemy import create_engine

if __name__ == '__main__':
    # How to find missing values in the secondary table
    # Find Rows in Source DF Which Are Not Available in New DF
    CONN_STR = 'postgresql+psycopg2://data_scientist:ds_secret@venus.arz.team:5436/mix_db'
    MARKET_ENGINE = create_engine(CONN_STR)
    QUERY = """
    SELECT TIME FROM created_price_src
    """
    mdf = pd.read_sql(QUERY, MARKET_ENGINE)
    print(mdf)

    CONN_STR = 'postgresql+psycopg2://data_scientist:ds_secret@venus.arz.team:5435/blocks'
    BLOCK_ENGINE = create_engine(CONN_STR)
    QUERY = """
    SELECT TIME FROM btc_network_info
    """
    bdf = pd.read_sql(QUERY, BLOCK_ENGINE)
    bdf.time = pd.to_datetime(bdf.time, unit='s', utc=pytz.utc)
    print(bdf)

    df = pd.merge(bdf, mdf, on='time', how='outer',  indicator=True)
    print(df[df['_merge'] == 'left_only'])
    # Read more at: https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/
    df = bdf.merge(mdf, how='outer', indicator=True).loc[lambda x: x['_merge'] == 'left_only']
    print(df)
