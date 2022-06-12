
import datetime
from psycopg_pool import ConnectionPool

connection = {
    'host': 'venus.arz.team',
    'user': 'data_scientist',
    'password': 'ds_secret',
    'port': 5435,
    'dbname': 'blocks'
}
conninfo = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(**connection)

if __name__ == '__main__':
    begin_time = datetime.datetime.now()
    pool = ConnectionPool(conninfo,max_size=100,min_size=100,open=False)
    pool.open()
    with pool.connection() as conn:
        ps = conn.execute('SELECT * FROM block_stats limit 10;').fetchall()
    pool.close()
    print(datetime.datetime.now() - begin_time)