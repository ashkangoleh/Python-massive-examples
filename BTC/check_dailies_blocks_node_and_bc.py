"""
    Check validity and reliability of data in SDB
    Author : AshkanGolehPour
    Date : Sun 24 Apr 14:10 LocalTime
    
    
    
    Last modified validate data from blockchair and full node:
            validated data by 1 days differently
"""


import asyncpg
import asyncio
import time
from datetime import datetime

async def main():
    """check blocks count from blockchair and full node
    """
    #start time before run 
    start = time.monotonic()
    # databases url blockchair as BC and full node as NODE
    DATABASE_URL_BC = 'postgresql://data_scientist:ds_secret@venus.arz.team:5532/blockchair'
    DATABASE_URL_NODE = 'postgresql://data_scientist:ds_secret@venus.arz.team:5435/blocks'
    #asyncpg connections by create_pool to improve queries and performance
    conn_bc = await asyncpg.create_pool(DATABASE_URL_BC)
    conn_node = await asyncpg.create_pool(DATABASE_URL_NODE)
    # fetch all rows from blockchair and full node by raw query
    fetch_bc = await conn_bc.fetch("select date_trunc('DAY',time) as day,count(id) as blocks_count from blocks group by day order by day desc;")
    fetch_node = await conn_node.fetch("select date_trunc('DAY',to_timestamp(time)) as day,count(height) as blocks_count from btc_network_info group by day order by day desc;")
    # result rows as a list by filter columns
    result_bc = [[row['day'].strftime('%s'),row['blocks_count']] for row in fetch_bc]
    result_node = [[row['day'].strftime('%s'),row['blocks_count']] for row in fetch_node]
    # filter (union) blockchair and full node to find missed days
    match = list(filter(lambda x: x not in result_bc, result_node))
    #transformed unix time to formatstring time plus blocks count
    print('match: ', [(datetime.utcfromtimestamp(
        int(y[0])).strftime('%Y-%m-%d'),y[1]) for y in match])
    #end time after run 
    end = time.monotonic()
    print(end - start)
    #closing connections
    await conn_bc.close()
    await conn_node.close()

asyncio.get_event_loop().run_until_complete(main())
