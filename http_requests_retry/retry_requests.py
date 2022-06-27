import requests
from requests.adapters import HTTPAdapter,Retry
import http
try:
    http.client.HTTPConnection.debuglevel = 1
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504,400],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    response = http.get("https://dp.d01.arz.team/api/ohlcv/v1")
    print('response: ', response)
except requests.RequestException as e:
    print(e)