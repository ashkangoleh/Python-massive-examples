import json
from threading import Thread
import time
import websocket


class KuCoinWebSocket:
    def __init__(self, proxies=None):
        self.proxies = proxies
        self.ws = websocket.WebSocketApp("wss://ws-api-spot.kucoin.com/?token=2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJ9Hh-c6oTwHaTAzKEalUHZBtEGV5c-QE4diYB9J6i9GjsxUuhPw3BlrzazF6ghq4L_M52Kxmq3kMMB_cVC6NnqQ=.lQHa-6XHLnJ6GU_S507GBw==&connectId=75c4d7e949224f49b019025bf4414fb0",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open,
                                         header={
                                             "User-Agent": "KuCoinWebSocketClient"},
                                         )

    def on_message(self, ws, message):
        ws.send(json.dumps({
                       "type": 'subscribe',
                        "topic": "/market/candles:BTC-USDT_1hour",
                        "response": True
                    }))
        print(json.loads(message))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            while True:
                time.sleep(2)
                ws.send(json.dumps({"type": "ping"}))
        Thread.start_new_thread(run, ())

    def start(self):
        self.ws.run_forever()


cont = KuCoinWebSocket()

cont.start()
