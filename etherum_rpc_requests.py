import requests




headers = {
    'Content-Type': 'application/json',
}

# data = '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'
# data = '{"jsonrpc":"2.0","method":"eth_mining","params": [],"id":1}'
# data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": [14144037,false],"id":1}'
data = '{"method":"trace_callMany","params":[[[{"from":"0x407d73d8a49eeb85d32cf465507dd71d507100c1","to":"0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b","value":"0x186a0"},["trace"]],[{"from":"0x407d73d8a49eeb85d32cf465507dd71d507100c1","to":"0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b","value":"0x186a0"},["trace"]]],"latest"],"id":1,"jsonrpc":"2.0"}'

response = requests.post('http://venus.arz.team:8645/',
                         headers=headers, data=data)
print('response: ', response.json())
# result = response.json()['result']
# print('result: ', result)
# print('difficulty:(from jsonrpc)->', result['difficulty'])
# print('miner:(from jsonrpc)->', result['miner'])
# print("*"*50)
# print("*"*50)
# print('difficulty:(convert to int from HexByte)->',
#       int(result['difficulty'], 0))



# response = requests.post('https://mainnet.infura.io/v3/af65e73fbd204ffca9b4256e9f231e38', headers=headers, data=data)
# print('response: ', response.json())