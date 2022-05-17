import requests
import json
from requests.auth import HTTPBasicAuth
import datetime
import pytz

headers = {
    'content-type': 'text/plain;',
}
block_id = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
block_height = 349584
# auth = HTTPBasicAuth('bitcoin_rpc_user', 'W31DEMtbKdbim')
auth = HTTPBasicAuth('admin', '1')
getblock = '{"method":"getblock","params": ["%s"],"id": 1}' % (block_id)
getblockstats = '{"jsonrpc": "1.0", "id": "curltest", "method": "getblockstats", "params": [%d, ["blockhash","subsidy", "time", "totalfee"]]}' %(block_height)
response_getblock = requests.post('http://localhost:8332',
                                  headers=headers, data=getblock, auth=auth)
response_blockstats = reqresponse_getblock = requests.post('http://localhost:8332',
                                                           headers=headers, data=getblockstats, auth=auth)


getBlockstats_final_result = {}
getblock_final_result= {}
getBlockstats_final_result['result'] = {
    "block_id": response_blockstats.json()["result"]['blockhash'],
    "subsidy": float(int(response_blockstats.json()["result"]['subsidy'] / 1e8)),
    "time": str(datetime.datetime.fromtimestamp(response_blockstats.json()["result"]['time'],tz=pytz.utc)),
    "totalfee": response_blockstats.json()["result"]['totalfee']
}
print(f"getblockstats_: {json.dumps(getBlockstats_final_result, indent=4)}",end=f"\n{'*'*100}\n")
print(f"getblock_: {json.dumps(response_getblock.json(), indent=4)}")
