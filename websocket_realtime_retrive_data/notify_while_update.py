import asyncio
import aiopg
import psycopg2


def get_latest_data():
    conn = psycopg2.connect(dsn='dbname=fastifyApiPrac user=root password=1 host=arz.local port=5432')
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT * FROM public."Users" ORDER BY id DESC LIMIT 2')
    result = cur.fetchall()
    return dict(result[-1])


async def get_last_data():
    conn = await aiopg.connect(dsn='dbname=fastifyApiPrac user=root password=1 host=arz.local port=5432',enable_json=True)
    cur = await conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # set up a trigger function to notify when table is updated
    # await cur.execute('CREATE FUNCTION notify_on_users_change() RETURNS TRIGGER AS $$ BEGIN NOTIFY users_change; RETURN NEW; END; $$ LANGUAGE plpgsql;')
    # create a trigger to call the notify function
   # await cur.execute('CREATE TRIGGER users_change_trigger AFTER INSERT OR UPDATE OR DELETE ON public."Users" FOR EACH ROW EXECUTE FUNCTION notify_on_users_change();')
    # listen for notifications
    await cur.execute("LISTEN users_change;")
    while True:
        # fetch the last data each time the table updates
        await cur.execute('SELECT * FROM public."Users" ORDER BY id DESC LIMIT 1')
        result = await cur.fetchone()
        dict_result = dict(result)
        # wait for notification
        conn.notifies
        print("==>> dict_result: ", dict_result)
        await asyncio.sleep(1)
    await cur.close()
    conn.close()


async def main():
    task = asyncio.create_task(get_last_data())
    await asyncio.gather(task)

asyncio.run(main())
