from datetime import datetime, timedelta
import time
import requests as req
# from functools import cache,lru_cache
import json
import requests_cache
from threading import Thread
# pip install requests-cache

# session = CachedSession(
#     'demo_cache',
#     use_cache_dir=True,                # Save files in the default user cache dir
#     cache_control=True,                # Use Cache-Control headers for expiration, if available
#     expire_after=timedelta(days=1),    # Otherwise expire responses after one day
#     allowable_methods=['GET', 'POST'], # Cache POST requests to avoid sending the same data twice
#     allowable_codes=[200, 400],        # Cache 400 responses as a solemn reminder of your failures
#     ignored_parameters=['api_key'],    # Don't match this param or save it in the cache
#     match_headers=True,                # Match all request headers
#     stale_if_error=True,               # In case of request errors, use stale cache data if possible
# )


# @lru_cache(maxsize=2048)
def getRequest(url):
    try:
        se = req.session()
        # session = requests_cache.CachedSession(
        #     'demo_cache', use_cache_dir=True, expire_after=timedelta(seconds=10))
        params = {
            "symbol": "BTC-USDT"
        }

        data = se.get(url)
        print("==>> data: ", data.status_code)
        if data.status_code == 200:
            return json.dumps(data.json(), indent=4)
        else:
            print("HTTP ERROR: 429")
    except req.HTTPError as e:
        print("==>> HTTPError: ", e)

start = time.time()
for i in range(60000):
    url = 'https://api.nobitex.ir/v2/orderbook/BTCIRT'
    s = Thread(target=getRequest,args=(url,))
    s.start()
end = time.time() - start

print("==>> end: ", end)
