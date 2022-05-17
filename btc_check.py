from numpy import block
import psycopg2
import logging
from datetime import datetime
import pandas as pd
import pytz
url = 'postgresql://ds:987a1d66a1d411eca0462fd85b4c826f@venus.arz.team:5435/blocks'


def connectDb(URL):
    try:
        engine = psycopg2.connect(URL)
        return engine
    except psycopg2.OperationalError as e:
        logging.error(e)


connection = connectDb(url)
try:
    with connection.cursor() as cur:
        cur.execute(
            """SELECT height, time FROM block_header WHERE to_timestamp(time) between '2022-03-01' and  '2022-03-01 23:59:59'""")
        test = cur.fetchall()
        block_header = pd.DataFrame(test)
        block_header.rename(columns={
            0: 'Block_id',
            1: 'DateTime'
        }, inplace=True)
        # block_header['DateTime'] = block_header['DateTime'].apply(
        #     lambda x: datetime.fromtimestamp(x))
        block_header['DateTime'] = pd.to_datetime(block_header['DateTime'],utc=pytz.utc,unit='s')
    print(block_header)

except Exception as e:
    logging.error(e)
finally:
    cur.close()
    connection.close()

