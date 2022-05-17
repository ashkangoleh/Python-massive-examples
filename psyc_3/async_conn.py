import psycopg
import datetime
import asyncio
from psycopg.rows import dict_row

connection = {
    'host': 'venus.arz.team',
    'user': 'data_scientist',
    'password': 'ds_secret',
    'port': 5435,
    'dbname': 'blocks'
}
conninfo = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(**connection)



async def main():
    try:
        aconn = await psycopg.AsyncConnection.connect(conninfo=conninfo,row_factory=dict_row)
        async with aconn:
            async with aconn.cursor() as cur:
                ps = await cur.execute('SELECT * FROM block_stats limit 10;')
                result = await ps.fetchall()
        await aconn.close()
        return result
    except psycopg.ConnectionError as e:
        raise e

if __name__ == '__main__':
    
    begin_time = datetime.datetime.now()
    async_result = asyncio.run(main())
    print('ps: ', async_result)
    print(datetime.datetime.now() - begin_time)

