import json
from sqlite3 import connect
import time
import websockets as ws
import asyncio
import requests as req


def get_public_key():
    url: str = "https://api.kucoin.com/api/v1/bullet-public"
    resp: json = req.post(url=url).json()
    _ws_connection: str = f"{resp['data']['instanceServers'][0]['endpoint']}?token={resp['data']['token']}"
    _ws_details: int = resp['data']['instanceServers'][0]['pingTimeout']
    return _ws_connection, _ws_details
# async def send_message(self, msg, retry_count=0):
#     if not self._socket:
#         if retry_count < 5:
#             await asyncio.sleep(1)
#             await self.send_message(msg, retry_count + 1)
#     else:
#         msg['id'] = str(int(time.time() * 1000))
#         msg['privateChannel'] = self._private
#         await self._socket.send(json.dumps(msg))


def _get_ws_pingtimeout(details):
    if not details:
        raise Exception("Unknown Websocket details")

    ping_timeout = int(details / 1000 / 2) - 1
    return ping_timeout


async def send_ping(socket):
    msg = {
        'id': str(int(time.time() * 1000)),
        'type': 'ping'
    }
    await socket.send(json.dumps(msg))
    last_ping = time.time()
    return last_ping


async def handler():
    connection, details = get_public_key()
    async with ws.connect(connection) as channel:
        last_ping = await send_ping(channel)
        while True:
            if time.time() - last_ping > _get_ws_pingtimeout(details):
                await send_ping(channel)
            try:
                topics = {
                    "BTC-USDT": "BTC-USDT",
                    "ETH-USDT": "ETH-USDT",
                }   
                topic = 'BTC-USDT'
                subscribe = {
                    "id": 1545910660739,
                    "type": "subscribe",
                    "topic": f'/market/level2:{topic}',
                    "privateChannel": False,
                    "response": True
                }
                unsubscribe ={
                    # "id":subscribe.get('id'),
                    'type': 'unsubscribe',
                    'topic': topic,
                    'response': True
                }
                await channel.send(json.dumps(subscribe))
                result = await channel.recv()
                result = json.loads(result)
                print("==>> result: ", result)
                await asyncio.sleep(5)
                # if result["type"] == "ack":
                #     await channel.send(json.dumps(unsubscribe))
                #     print("result unsubscribe: ", result["type"])
            except Exception as e:
                raise e


if __name__ == "__main__":
    asyncio.run(handler())
