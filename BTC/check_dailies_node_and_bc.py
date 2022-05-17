"""
    Check validity and reliability of data in SDB
    Author : AshkanGolehPour
    date : Sun 24 Apr 14:10 LocalTime
    
    
    
    last modified data from blockchair:
            blocks -> 4853
            transactions -> 4853
            outputs -> 4853
            inputs -> 4851
"""

import asyncpg
import asyncio
import time
import logging
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta


async def validate_day():
    now = datetime.now()
    last_day = timedelta(days=1)
    return now - last_day


def blockchair_source_count(content):
    try:
        url = f'https://gz.blockchair.com/bitcoin/{content}/'
        r = requests.get(url)
        page = r.text
        soup = BeautifulSoup(page, features="html.parser")
        a_tags = soup.find_all('a', {'href': re.compile(r'tsv.gz$')})
        urls = list(map(lambda x: url + x.get('href'), a_tags))
        return urls.__len__()
    except Exception as e:
        logging.error(e)


async def main():
    response = {}
    data = ["blocks", "transactions", "inputs", "outputs"]
    response['counts_from_urls'] = {i: blockchair_source_count(i) for i in data}
    ploto_db = ["inputs", "outputs"]
    venus_db = ["blocks", "transactions"]
    valid_date = await validate_day()
    response['Now'] = str(datetime.now())
    response['validate_date'] = valid_date
    for names in venus_db:
        start = time.monotonic()
        DATABASE_URL = 'postgresql://data_scientist:ds_secret@venus.arz.team:5532/blockchair'
        conn = await asyncpg.create_pool(DATABASE_URL)
        result = await conn.fetch(f"SELECT date_trunc('DAY',time) as day FROM {names} where time >= $1", valid_date)
        response[f'{names}_missed_days_count']= set(result).__len__()
        end = time.monotonic()
        response[f'{names}_time_taken'] = end - start
        await conn.close()
    for names in ploto_db:
        start = time.monotonic()
        DATABASE_URL = 'postgresql://data_scientist:ds_secret@ploto.arz.team:5532/blockchair'
        conn = await asyncpg.create_pool(DATABASE_URL)
        result = await conn.fetch(f"SELECT date_trunc('DAY',time) as day FROM {names} where time >= $1", valid_date)
        response[f'{names}_missed_days_count']= set(result).__len__()
        end = time.monotonic()
        response[f'{names}_time_taken'] = end - start
        await conn.close()
    print(response)

asyncio.get_event_loop().run_until_complete(main())
