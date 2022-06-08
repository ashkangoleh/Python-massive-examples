import requests
import json

COIN_URL = "http://atlasapi.ir/api/signal/"
COIN_PASSWORD = "B9e1H4z3A4D3A9t8las"
TIME_FRAME_LIST = [5, 15, 30, 60, 120, 240, 360, 720, 1440, 10080]


def coinAPI(url, password, time_frame, exchange):
    params = {
        "password": password,
        "time_frame": time_frame,
        "exchange": exchange,
        "marketType": "spot"
    }
    res = requests.get(url, params=params)
    response = res.json()
    pairs = {}
    for i in response:
        pairs[i['symbol']] = i['buy'] if i['buy'] == 1 else ''
    return response
    # return pairs


payload = coinAPI(url=COIN_URL, password=COIN_PASSWORD,
                  time_frame=10080, exchange='kucoin')
print('payload: ', payload)

with open("./kucoin-spot-1m.json", "w+") as file:
    file.write(json.dumps(payload, indent=4))
