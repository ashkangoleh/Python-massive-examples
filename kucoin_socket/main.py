import asyncio
from curses.ascii import isupper
from time import time
import websockets as ws
import requests
import multiprocessing
import time
import json
from uuid import uuid4


class KucoinWs():

    def __init__(self, queue: multiprocessing = None, topics=[]) -> None:
        self.token: str = ''
        self.queue: multiprocessing = queue
        self.endpoint: str = ''
        self.connectId: str = ''
        self.wsEndpoint: str = ''
        self.ping_interval:int = 50000
        self.timeout: int = 0
        self.topics: list = topics
        self.last_ping: float = time.time()
        self.keep_waiting: bool = True
        self.http_proxy: dict = {
            "http_proxy_host": "https://94.26.108.67",
            "http_proxy_port": 2580,
        }

    def get_ws(self) -> str:
        response: json = requests.post(
            'https://api.kucoin.com/api/v1/bullet-public').json()
        self.token = response['data']['token']
        self.endpoint = response['data']['instanceServers'][0]['endpoint']
        self.timeout = int(response['data']['instanceServers']
                           [0]['pingTimeout'] / 1000) - 2
        print("==>> self.timeout: ", self.timeout)
        self.connectId = str(uuid4()).replace('-', '')
        wsEndpoint = f"{self.endpoint}?token={self.token}&connectId={self.connectId}"
        self.wsEndpoint = wsEndpoint


    async def get_id(self) -> ws:
        async with ws.connect(self.wsEndpoint) as websocket:
            message: str = await websocket.recv()
            self.connectId = message.split(',')[0].split(':')[
                1].replace('"', '')
            await websocket.close()

    async def _run(self) -> ws:
        li = []
        try:
            async with ws.connect(self.wsEndpoint,ping_interval=self.ping_interval) as websocket:
                for topic in self.topics:
                    await websocket.send(json.dumps({
                        "id": self.connectId,
                        "type": 'subscribe',
                        "topic": topic,
                        "response": True
                    }))

                    self.last_ping = time.time()

                while self.keep_waiting:
                    await asyncio.sleep(1.0)
                    if time.time() - self.last_ping > self.timeout:
                        print("here")
                        await websocket.send(json.dumps({
                            "id": self.connectId,
                            "type": 'ping'
                        }))
                    message: str = await websocket.recv()
                    message = json.loads(message)
                    if 'subject' in message.keys():
                        # if message['subject'].isupper():
                        li.append(message)
                        print("==>> message: ", message)
                        self.queue.put(message)
        except ws.ConnectionClosed:
            self.keep_waiting = False
            await websocket.send(json.dumps({
                "id": self.connectId,
                "type": 'ping'
            }))
            message: str = await websocket.recv()
            print("==>> message: ", message)
        print(li.__len__())


async def main() -> KucoinWs:
    q: multiprocessing.Queue = multiprocessing.Queue()
    _ws: KucoinWs = KucoinWs(
        q, ['/market/ticker:all', '/market/level2:BTC-USDT'])
    _ws.get_ws()
    print(True if isinstance(_ws.wsEndpoint, str) else False)
    await _ws.get_id()
    _ws.get_ws()
    await _ws._run()


def run() -> asyncio:
    asyncio.run(main())


if __name__ == '__main__':
    run()
