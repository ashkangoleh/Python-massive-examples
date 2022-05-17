from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://venus.arz.team:8645'))
print(w3.isConnected())
# for i in range(10):
#     getblock = w3.eth.get_transaction_by_block('latest',i)
#     with open('transaction_by_latest_block_number.json','a+') as file:
#         file.write(str(dict(getblock))+"\n")


print(w3.eth.get_block('latest'))