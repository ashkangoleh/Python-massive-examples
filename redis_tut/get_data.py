import json
import pandas as pd
from datetime import datetime
from typing import Union
import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
import asyncio
from redis_om import get_redis_connection, HashModel

redis_db = get_redis_connection(
    host="localhost", port=6379
)
ASSET = {"ex": [
    "Binance",
    "Binanceusdm",
    "Bitfinex",
    "Bitmex",
    "Bybit",
    "BybitPerpetual",
    "Coinbasepro",
    "Coinex",
    "CoinexPerpetual",
    "Deribit",
    "Ftx",
    "Gateio",
    "Huobi",
    "Kraken",
    "Kucoin",
    "Kucoinfutures",
    "Okex",
    "Poloniex",
],
    "reso": [
    "5m",
    "1h",
    "1d"
]
}


def assets_pair(exchange: str = "kucoin:spot"):
    try:
        category = exchange.split(":")[1]
        exchange = exchange.split(":")[0]
        with open(f"./assets/assets_{category}_{exchange}.txt", "r+") as asset:
            _list = asset.read().splitlines()
            return _list
    except Exception as e:
        pass


async def extract_from_arz_market(client: aiohttp.ClientSession, symbol: str, interval: str, start_time: Union[int, str, datetime],
                                  end_time: Union[int, str, datetime], exchange: str = "binance") -> Union[Exception, pd.DataFrame]:
    try:
        # https://docs.kucoin.com/?lang=en_US#get-klines
        api_address = "http://dp.voyager.arz.team/api/ohlcv/v1/"
        # api_address = "https://dp.d01.arz.team/api/ohlcv/v1"
        params = {
            "base": symbol.split("-")[0].lower(),
            "quote": symbol.split("-")[1].lower(),
            "resolution": interval,
            "exchange": exchange.split(":")[0],
            "from": start_time*1000,
            "to": end_time*1000
        }
        async with client.get(api_address, params=params) as resp:
            candles = await resp.json()
            # print('candles: ', candles[0]['source_id'], start_time,end_time)
            return candles
    except ClientConnectionError as e:
        raise e


async def extract_from_arz_market_async(interval: str, start_time: Union[int, str, datetime],
                                        end_time: Union[int, str, datetime], assets_list: list, exchange: str = "binance:spot"):
    try:
        async with aiohttp.ClientSession() as client:
            # Generate a list of coroutines for each request we want to make:
            # requests = [asyncio.ensure_future(fetch(client, symbol)) for symbol in lists]
            data = {}
            for i in asset_list:
                data[i] =  await extract_from_arz_market(client=client, symbol=i, interval=interval,
                                                          exchange=exchange,
                                                          start_time=start_time,
                                                          end_time=end_time,
                                                          )
                
            # req = [*requests]
            # print('req: ', data)
            req_str = json.dumps(data)
            # print('requests: ',await asyncio.gather(*requests))
            redis_db.set(f"{exchange}:{interval}",value=req_str)
            # # # Wait for all requests to complete
            # try:
            #     df = pd.DataFrame(tuple(requests[0]),
            #                       columns=['source_id','timestamp', 'open', 'close', 'high', 'low', 'volume'])
            #     # print('df: ', df.to_dict(orient='records'))

            #     data.extend(df.to_dict(orient='records'))
            #     # print(json.dumps(data))
            #     # print('df: ', df)

            #     return None, df
            # except ConnectionAbortedError as err:
            #     print('err: ', err)
            #     return err, None
            # finally:
            #     redis_db.delete("test1")
            #     redis_db.lpush("test1",json.dumps(data[0]))
    except Exception as e:
        print('e(outer main): ', e)
        pass
if __name__ == '__main__':
    start = datetime.now()
    print('start: ', start)
    for reso in ASSET['reso']:
        for name in ASSET['ex']:
            asset_list = assets_pair(exchange=f"{name.lower()}:spot")[:1]
            params = {
                "interval": reso,
                # "exchange": exchange.split(":")[0],
                "exchange": f"{name.lower()}",
                "start_time": 1655902274,
                "end_time": 1656302274,
                "assets_list": asset_list
            }
            # print('params: ', params)
            # print('params: ', params)
            asyncio.run(extract_from_arz_market_async(**params))
            # res = redis_db.get("binance")
            # res = json.loads(res)
            # print('res: ', res)
    end = datetime.now() - start
    print('end: ', end)
