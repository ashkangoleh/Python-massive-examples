import time
import multiprocessing
import requests
import json
from threading import Thread
from multiprocessing import Process
RPCUSER = "bitcoin_rpc_user"
RPCPASSWORD = "W31DEMtbKdbim"
URL = "http://venus.arz.team:10082"
# raw


def rawMemPool():
    data_raw_mempool = '{"jsonrpc": "2.0", "id":"curltest", "method": "getrawtransaction", "params": ["4ffe2978216050ad89a8406231f1d9903ce6b8cca3452f2c78cbefc37f47ab7f",2] }'
    # data_raw_mempool = '{"jsonrpc": "2.0", "id":"curltest", "method": "getblockchaininfo", "params": [] }'
    response_raw_mempool = requests.post(
        URL, data=data_raw_mempool,  auth=(RPCUSER, RPCPASSWORD))
    return response_raw_mempool.json()


# ancestors ,setting true to complete details
# data = '{"jsonrpc": "2.0", "id":"curltest", "method": "getmempoolancestors", "params": ["a926c8160584b8aabf244ad2ae2bc54a590857169faf148e02c39ea2e3f6dc66",true] }'
# data = '{"jsonrpc": "2.0", "id":"curltest", "method": "getmempooldescendants", "params": ["a926c8160584b8aabf244ad2ae2bc54a590857169faf148e02c39ea2e3f6dc66",true] }' #descendants ,setting true to complete details
# entry ,setting true to complete details
start_time = time.time()
print(json.dumps(rawMemPool(), indent=4))
# with open("mempool.json", "w+") as file:
#           file.write(f"{json.dumps(rawMemPool(),indent=4)}")
# print('recent_raw_mempool: ', recent_raw_mempool.__len__())
# try:
#     result = []
#     counter = 0
#     while counter <= recent_raw_mempool.__len__():
#         data_mempool_entry = '{"jsonrpc": "2.0", "id":"curltest", "method": "getmempoolentry", "params": ["%s"] }' % (
#             recent_raw_mempool[counter])
#         response_mempool_entry = requests.post(URL, data=data_mempool_entry,
#                                                auth=(RPCUSER, RPCPASSWORD))
#         if response_mempool_entry.json()['result']['fee'] is not None:
#             result.append({
#                 "txid": recent_raw_mempool[counter],
#                 "fee": response_mempool_entry.json()['result']['fee'],
#                 "timestamp": response_mempool_entry.json()['result']['time'],
#             })
#         else:
#             result.append({
#                 "txid": recent_raw_mempool[counter],
#                 "fee": 0,
#                 "timestamp": response_mempool_entry.json()['result']['time'],
#             })
#         counter = counter + 1
#         if counter > recent_raw_mempool.__len__():
#             break
# except Exception as e:
#     print(e)


# print(json.dumps(result, indent=4))
# print(result.__len__())
# end_time = time.time()
# print(f"time taken:{end_time - start_time}")
