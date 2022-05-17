import psycopg
import datetime
from psycopg.rows import dict_row

connection = {
    'host': 'venus.arz.team',
    'user': 'data_scientist',
    'password': 'ds_secret',
    'port': 5435,
    'dbname': 'blocks'
}
conninfo = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
    **connection)

if __name__ == '__main__':
    conn = psycopg.connect(**connection, row_factory=dict_row)
    begin_time = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute('SELECT * FROM block_stats limit 10;')
    ps = cur.fetchall()
    print(ps)
    cur.close()
    print(datetime.datetime.now() - begin_time)


