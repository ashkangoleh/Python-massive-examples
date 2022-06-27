from time import sleep
from websocket import create_connection
import json

# pip install websocket-client

# Launch the connection to the server.
ws = create_connection(
    'wss://streamer.cryptocompare.com/v2?api_key=1c171e50d1ee8a585f4780cd1eeac83390592869fa0201c97a0b315d59f7561c')

# Perform the handshake.
ws.send(json.dumps({"action": "SubAdd", "subs": ["11~BTC", "21~BTC", "5~CCCAGG~BTC~USD", "11~ETH", "21~ETH", "5~CCCAGG~ETH~USD", "11~BCH", "21~BCH", "5~CCCAGG~BCH~USD",
                    "11~EOS", "21~EOS", "5~CCCAGG~EOS~USD", "11~XRP", "21~XRP", "5~CCCAGG~XRP~USD", "11~LTC", "21~LTC", "5~CCCAGG~LTC~USD",
                                                 "11~ETC", "21~ETC", "5~CCCAGG~ETC~USD", "11~BSV", "21~BSV", "5~CCCAGG~BSV~USD", "11~LINK", "21~LINK", "5~CCCAGG~LINK~USD", "11~ATOM", "21~ATOM", "5~CCCAGG~ATOM~USD"]}))

# Printing all the result
while True:
    try:
        sleep(1)
        result = ws.recv()
        print(json.loads(result))
    except Exception as e:
        print(e)
        break
