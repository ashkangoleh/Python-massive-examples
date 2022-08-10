import asyncio
import json
import time
import websockets as ws
import requests as req
import logging
from exceptions import *
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class KucoinSocketManagerPrivateException(Exception):
    pass

async def get_public_key():
    url = "https://api.kucoin.com/api/v1/bullet-public"
    resp = req.post(url=url).json()
    return "wss://push1-v2.kucoin.com/endpoint?token=%s" % resp['data']['token']


class KucoinWebsocket:

    MAX_RECONNECTS = 5
    MAX_RECONNECT_SECONDS = 60
    MIN_RECONNECT_WAIT = 0.1
    TIMEOUT = 10
    PROTOCOL_VERSION = '1.0.0'

    def __init__(self, loop, coro, private=False):
        self._coro = coro
        self._loop = loop
        self._log = logging.getLogger(__name__)
        self._conn = None
        self._connect_id = None
        self._last_ping = None
        self._socket = None
        self._ws_details = self.get_public_key
        self._ws_endpoint = f"{self.get_public_key['data']['instanceServers'][0]['endpoint']}?token={self.get_public_key['data']['token']}"
        self._connect()

    def _connect(self):
        self._conn = asyncio.ensure_future(self._run(), loop=self._loop)

    @property
    def get_public_key(self):
        url = "https://api.kucoin.com/api/v1/bullet-public"
        resp = req.post(url=url).json()
        return resp

    @property
    def _get_ws_pingtimeout(self):

        if not self._ws_details:
            raise Exception("Unknown Websocket details")

        ping_timeout = int(
            self._ws_details['instanceServers'][0]['pingTimeout'] / 1000 / 2) - 1
        return ping_timeout

    async def _run(self):

        keep_waiting = True
        self._last_ping = time.time()  # record last ping
        # get the websocket details

        async with ws.connect(self._ws_details) as socket:
            self._socket = socket
            self._reconnect_attempts = 0

            try:
                while keep_waiting:
                    if time.time() - self._last_ping > self._get_ws_pingtimeout:
                        await self.send_ping
                    try:
                        evt = await asyncio.wait_for(self._socket.recv(), timeout=self._get_ws_pingtimeout())
                        print("==>> evt: ", evt)
                    except asyncio.TimeoutError:
                        self._log.debug("no message in {} seconds".format(
                            self._get_ws_pingtimeout()))
                        await self.send_ping

            except ws.ConnectionClosed:
                keep_waiting = False

    @property
    async def send_ping(self):
        msg = {
            'id': str(int(time.time() * 1000)),
            'type': 'ping'
        }
        await self._socket.send(json.dumps(msg))
        self._last_ping = time.time()

    async def cancel(self):
        try:
            self._conn.cancel()
        except asyncio.CancelledError:
            pass


class KucoinSocketManager:

    PRIVATE_TOPICS = [
        '/account/balance'
    ]

    def __init__(self):
        """Initialise the IdexSocketManager
        """
        self._callback = None
        self._conn = None
        self._loop = None
        self._client = None
        self._private = False
        self._log = logging.getLogger(__name__)

    @classmethod
    async def create(cls, loop, callback, private=False):
        self = KucoinSocketManager()
        self._loop = loop
        self._private = private
        self._callback = callback
        self._conn = KucoinWebsocket(loop, self._recv, private)
        return self

    async def _recv(self, msg):
        if 'data' in msg:
            await self._callback(msg)

    async def subscribe(self, topic):
        """Subscribe to a channel
        :param topic: required
        :type topic: str
        :returns: None
        Sample ws response
        .. code-block:: python
            {
                "type":"message",
                "topic":"/market/ticker:BTC-USDT",
                "subject":"trade.ticker",
                "data":{
                    "sequence":"1545896668986",
                    "bestAsk":"0.08",
                    "size":"0.011",
                    "bestBidSize":"0.036",
                    "price":"0.08",
                    "bestAskSize":"0.18",
                    "bestBid":"0.049"
                }
            }
        Error response
        .. code-block:: python
            {
                'code': 404,
                'data': 'topic /market/ticker:BTC-USDT is not found',
                'id': '1550868034537',
                'type': 'error'
            }
        """

        req_msg = {
            'type': 'subscribe',
            'topic': topic,
            'response': True
        }

        if topic in self.PRIVATE_TOPICS and not self._private:
            raise KucoinSocketManagerPrivateException(
                "Initialise KucoinSocketManager with private=true for {} topic".format(
                    topic)
            )

        await self._conn.send_message(req_msg)

    async def unsubscribe(self, topic):
        """Unsubscribe from a topic
        :param topic: required
        :type topic: str
        :returns: None
        Sample ws response
        .. code-block:: python
            {
                "id": "1545910840805",
                "type": "ack"
            }
        """

        req_msg = {
            'type': 'unsubscribe',
            'topic': topic,
            'response': True
        }

        await self._conn.send_message(req_msg)


async def main():
    global loop

    ww = await KucoinSocketManager.create(loop,'/market/ticker:ETH-USDT')
    result = await ww.subscribe('/market/ticker:ETH-USDT')
    print("==>> result: ", result)
if __name__ == "__main__":
    loop.run_until_complete(main())
