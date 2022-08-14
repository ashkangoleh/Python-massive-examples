import asyncio
import json
import time
import unittest
from main import KucoinWs
import websocket as ws


def async_run(coroutine):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coroutine(*args, **kwargs))
        finally:
            loop.close()
    return wrapper


class KucoinWsTest(unittest.TestCase):
    # ws.enableTrace(True)
    WS = ws.WebSocket()
    _WS = KucoinWs(topics=['/market/ticker:all',
                           '/market/level2:BTC-USDT'])

    ENDPOINT: str = ''
    
    def on_error(self,ws, error):
        print("==>> error: ", error)
        
    def test_endpoint_validity(self):
        self._WS.get_ws()
        KucoinWsTest.ENDPOINT = self._WS.wsEndpoint
        self.assertIsNotNone(self._WS.wsEndpoint)

    @async_run
    async def test_get_id(self):
        await self._WS.get_id()
        self.assertIsNotNone(self._WS.get_id)

    @async_run
    async def test_connectivity(self):
        self.test_endpoint_validity()
        # async with ws.connect(self._WS.wsEndpoint, **self._WS.http_proxy) as websocket:
        try:
            while 1:
                channel = ws.WebSocketApp(KucoinWsTest.ENDPOINT,on_error=self.on_error)
                # channel.run_forever(**self._WS.http_proxy)
                channel.send({
                    "id": int(time.time()*1000),
                    "type": 'ping'
                })
                result = ws.recv()
                print("==>> result: ", result)
        except ws.WebSocketConnectionClosedException as e:
            import traceback
            print(traceback.format_exc())
