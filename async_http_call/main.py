import asyncio
from datetime import datetime, timedelta
import requests
import aiohttp

lists = ['btc-usdt', 'eth-usdt', 'doge-usdt', 'eth-btc']


async def fetch(client, symbol):
    print('symbol: ', symbol)
    api_address = "https://dp.voyager.arz.team/api/ohlcv/v1"
    interval = '1h'
    exchange = 'kucoin'
    start_time = '2022-06-18'
    start_time = int(datetime.fromisoformat(start_time).timestamp())
    end_time = int(datetime.today().timestamp())

    params = {
        "base": symbol.split("-")[0].lower(),
        "quote": symbol.split("-")[1].lower(),
        "resolution": interval,
        "exchange": exchange,
        "from": start_time * 1000,
        "to": end_time * 1000
    }
    async with client.get(api_address, params=params) as resp:
        assert resp.status == 200
        response = await resp.json()
        return response


async def main():
    try:
        async with aiohttp.ClientSession(  headers={
            "Content-Encoding":"gzip"
        }) as client:
            # Generate a list of coroutines for each request we want to make:
            # requests = [asyncio.ensure_future(fetch(client, symbol)) for symbol in lists]
            requests = [await fetch(client, symbol) for symbol in lists]
            # Wait for all requests to complete
            return await asyncio.gather(*requests)
    except Exception as e:
        pass

if __name__ == '__main__':
    # aiohttp uses non-blocking sockets
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    
    # requests uses blocking sockets
    time_delta = datetime.now() - timedelta(days=3)
    print('time_delta: ', time_delta)
    next_time = datetime.now() + timedelta(days=1)
    print('next_time: ', next_time)
    for symbol in ['btc-usdt', 'eth-usdt', 'doge-usdt', 'eth-btc']:
        print('symbol: ', symbol)
        params = {
            "base": symbol.split("-")[0].lower(),
            "quote": symbol.split("-")[1].lower(),
            "resolution": "1h",
            "exchange": "binance",
            "from": int(time_delta.timestamp()) * 1000,
            "to": int(next_time.timestamp()) * 1000
        }
        candles = requests.get(url="https://dp.d01.arz.team/api/ohlcv/v1", params=params)

        # print(candles.json(), '\n')
