import psycopg2
import psycopg2.extensions
import asyncio
import aiopg

# Connect to PostgreSQL
conn = psycopg2.connect(database='postgres', user='root',
                        password='1', host='arz.local', port='5454')

# Enable notification processing
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Open a channel to listen for notifications
channel = 'arzc'
table_name = 'cms_trained'
# cur = conn.cursor()
# cur.execute(f"LISTEN {channel}")
# cur.execute(
#     f"CREATE OR REPLACE FUNCTION notify_{channel}() RETURNS TRIGGER AS $$ BEGIN PERFORM pg_notify('{channel}', TG_OP || ' {table_name}'); RETURN NULL; END; $$ LANGUAGE plpgsql;")
# cur.execute(
#     f"CREATE TRIGGER {channel}_trigger AFTER INSERT OR UPDATE OR DELETE ON {table_name} FOR EACH ROW EXECUTE PROCEDURE notify_{channel}();")
print(
    f"Listening for notifications on channel {channel} for table {table_name}...")

# while True:
#     # Wait for notifications
#     if psycopg2.extensions.POLL_OK == conn.poll():
#         conn.commit()
#         notifications = conn.notifies
#         for notification in notifications:
#             print(notification)
#             print(f"Received notification: {notification.payload}")



async def get_last_data():
    conn = await aiopg.connect(dsn='dbname=postgres user=root password=1 host=arz.local port=5454',enable_json=True)
    cur = await conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # set up a trigger function to notify when table is updated
    # await cur.execute('CREATE FUNCTION notify_on_users_change() RETURNS TRIGGER AS $$ BEGIN NOTIFY users_change; RETURN NEW; END; $$ LANGUAGE plpgsql;')
    # create a trigger to call the notify function
   # await cur.execute('CREATE TRIGGER users_change_trigger AFTER INSERT OR UPDATE OR DELETE ON public."Users" FOR EACH ROW EXECUTE FUNCTION notify_on_users_change();')
    # listen for notifications
    await cur.execute(f"LISTEN {channel};")
    while True:
        # fetch the last data each time the table updates
        await cur.execute('SELECT * FROM public."cms_trained"')
        result = await cur.fetchone()
        dict_result = dict(result)
        # wait for notification
        print("==>> conn.notifies: ", conn.notifies)
        print("==>> dict_result: ", dict_result)
        await asyncio.sleep(1)
    await cur.close()
    conn.close()


async def main():
    task = asyncio.create_task(get_last_data())
    await asyncio.gather(task)

asyncio.run(main())