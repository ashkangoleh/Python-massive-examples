import asyncio
import aiopg

async def get_last_data():
    conn = await aiopg.connect(dsn='dbname=mydb user=myuser password=mypassword host=myhost port=5432')
    cur = await conn.cursor()
    while True:
        await cur.execute("SELECT * FROM mytable ORDER BY id DESC LIMIT 1")
        result = await cur.fetchone()
        print(result)
        await asyncio.sleep(1)
    await cur.close()
    conn.close()

asyncio.run(get_last_data())
