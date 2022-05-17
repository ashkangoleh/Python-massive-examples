import logging
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

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
        
        
print(blockchair_source_count('inputs'))