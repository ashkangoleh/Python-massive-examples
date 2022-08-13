import json
from sqlite3 import connect
import time
import websockets as ws
import asyncio
import requests as req

loop = asyncio.new_event_loop()



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

    ping_timeout = int(details / 1000 / 2) - 2
    print("==>> ping_timeout: ", ping_timeout)
    return ping_timeout


async def send_ping(socket):
    msg = {
        'id': str(int(time.time() * 1000)),
        'type': 'ping'
    }
    ping = time.time()
    await socket.send(json.dumps(msg))
    return ping


async def handler():
    keep_waiting = True
    connection, details = get_public_key()
    async with ws.connect(connection) as channel:
        try:

            topic = 'BTC-USDT,ETH-USDT'
            subscribe = {
                "id": time.time()*1000,
                "type": "subscribe",
                "topic": f'/market/level2:{topic}',
                "privateChannel": False,
                "response": True
            }
            unsubscribe = {
                # "id":subscribe.get('id'),
                'type': 'unsubscribe',
                'topic': topic,
                'response': True
            }
            if time.time() - 2 > _get_ws_pingtimeout(details):
                await channel.send(json.dumps({
                        "id": str(int(time.time() * 1000)),
                        "type": 'ping'
                }))
            await channel.send(json.dumps(subscribe))

            while keep_waiting:
                result = await channel.recv()
                # result = json.loads(result)
                print("==>> result: ", result)
                await asyncio.sleep(0.5)
                # if result["type"] == "ack":
                #     await channel.send(json.dumps(unsubscribe))
            else:
                await channel.send(json.dumps({
                    "id": str(int(time.time() * 1000)),
                    "type": 'ping'
            }))
        except ws.ConnectionClosed:
            keep_waiting = False
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    asyncio.run(handler())
