import asyncio
import json
import time
import unittest
from .main import KucoinWs
import websockets as ws
import enum


def jsonify(data: dict) -> json:
    return json.dumps(data)


def jsonParser(data):
    return json.loads(data)


def async_run(coroutine):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coroutine(*args, **kwargs))
        finally:
            loop.close()
    return wrapper


class KucoinWsTest(unittest.TestCase):
    _WS = KucoinWs(topics=['/market/ticker:all',
                           '/market/level2:BTC-USDT'])


    def on_error(self, ws, error):
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
        try:
            async with ws.connect(KucoinWsTest._WS.wsEndpoint) as channel:
                self.assertEqual(channel.state.value, 1)
        except ws.ConnectionClosed as e:
            import traceback
            print(traceback.format_exc())
            print(f"error: {e}")

    @async_run
    async def test_ping(self):
        try:
            async with ws.connect(KucoinWsTest._WS.wsEndpoint) as channel:
                await channel.send(jsonify({
                    "id": int(time.time()*1000),
                    "type": 'ping'
                }))
                result = await channel.recv()
                result = jsonParser(result)

                self.assertEqual(list(result.keys()), ["id", "type"])
                self.assertEqual(result['type'], "welcome")
        except ws.ConnectionClosed as e:
            import traceback
            print(traceback.format_exc())
            print(f"error: {e}")
