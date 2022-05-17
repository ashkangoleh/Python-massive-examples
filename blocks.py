import asyncio
from dis import code_info
from textwrap import indent
from pyparsing import rest_of_line
import requests
import json

headers = {
    'content-type': 'text/plain;',
}


def blockCount():
    data_block_count = '{"jsonrpc": "2.0", "id": "curltest", "method": "getblockcount", "params": []}'

    response_block_count = requests.post('http://venus.arz.team:10082', headers=headers,
                                         data=data_block_count, auth=('bitcoin_rpc_user', 'W31DEMtbKdbim'))
    return response_block_count.json()['result']


async def blockStatsBlockHashGiver(count):
    data_height = '{"jsonrpc": "2.0", "id": "curltest", "method": "getblockstats", "params": [%d]}' % (count)
    response_height = requests.post('http://venus.arz.team:10082', headers=headers,
                                          data=data_height, auth=('bitcoin_rpc_user', 'W31DEMtbKdbim'))
    return response_height.json()['result']['blockhash']


async def main():
    count = 1
    _blockCount = blockCount()
    while count <= _blockCount:
        try:
            blockHash = await blockStatsBlockHashGiver(count)
            data = '{"jsonrpc": "2.0", "id": "curltest", "method": "getblock", "params": ["%s",1]}' % blockHash
            response = requests.post('http://venus.arz.team:10082', headers=headers,
                                    data=data, auth=('bitcoin_rpc_user', 'W31DEMtbKdbim'))
            result = response.json()['result']
            result.pop('tx',None)
            result.pop('chainwork',None)
            result.pop('previousblockhash',None)
            result.pop('nextblockhash',None)
            with open('test.json','a+') as file:
                file.write(f'{result}\n')
            count += 1
            if count > _blockCount:
                break
            
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    asyncio.run(main())

        
    
