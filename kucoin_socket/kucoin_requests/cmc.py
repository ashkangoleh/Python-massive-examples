from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
    #   'start':'1',
    # "symbol": "BTC",
    'limit': '5000',
    # 'convert': 'USDT'
    "sort":"cmc_rank"
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c4ba6116-edee-4965-b56e-c9319e498c13',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.dumps(response.json(),indent=4)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


