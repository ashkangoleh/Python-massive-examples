from web3 import Web3

print(f"{'*'*75}\n\t\t\t\x1b[0:30;41mProviders\x1b[0m", end=f"\n{'*'*75}\n")
print(f"""\x1b[0;30;42mIPCProvider\x1b[0m \u2193 \nSummary: This provider handles interaction with an IPC Socket based JSON-RPC server.\nexample: w3 = Web3(Web3.IPCProvider('~/Library/Ethereum/geth.ipc')) \n\x1b[0;30;42mWebsocketProvider\x1b[0m  \u2193\nSummary: This provider handles interactions with an WS or WSS based JSON-RPC server.\nexample1: w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))\nexample2: w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546', websocket_timeout=60))\n\x1b[0;30;42mHTTPProvider\x1b[0m\nSummary: This provider handles interactions with an HTTP or HTTPS based JSON-RPC server.\nexample: w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))\nextra example:\tadapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)\n\t\tsession = requests.Session()\n\t\tsession.mount('http://', adapter)\n\t\tsession.mount('https://', adapter)\n\t\tw3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545', session=session))""",
      end=f"\n{'*'*75}\n")

w3 = Web3(Web3.HTTPProvider('http://168.119.0.182:8545'))
# w3 = Web3(Web3.WebsocketProvider('ws://168.119.0.182:8546'))
# ********************************************************************************************************************************************************************************************
print(
    f"\n{'*'*75}\n\t\t\t\x1b[0:30;41mWeb3 Properties\x1b[0m", end=f"\n{'*'*75}\n")
print('\x1b[0;30;42mweb3\x1b[0m isConnected: ',
      w3.isConnected(), end=f"\n{'*'*75}\n")
# eth.default_block -> The default block number that will be used for any RPC methods that accept a block identifier. Defaults to 'latest'.
eth_default_block = w3.eth.default_block
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_syncing" RPC Method && Returns either False if the node is not syncing or a dictionary showing sync status.
eth_syncing = w3.eth.syncing
print('\x1b[0;30;42mcurrentBlock synced\x1b[0m(eth_syncing): ',
      eth_syncing, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_mining" RPC Method && Returns boolean as to whether the node is currently mining.
eth_mining = w3.eth.mining
print('\x1b[0;30;42meth_mining\x1b[0m(eth_mining): ',
      eth_mining, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_hashrate" RPC Method && Returns the current number of hashes per second the node is mining with.
eth_hashrate = w3.eth.hashrate
print('\x1b[0;30;42meth_hashrate\x1b[0m(eth_hashrate): ',
      eth_hashrate, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_maxPriorityFeePerGas" RPC Method && Returns a suggestion for a max priority fee for dynamic fee transactions in Wei.
eth_max_priority_fee = w3.eth.max_priority_fee
print('\x1b[0;30;42meth_max_priority_fee\x1b[0m(eth_maxPriorityFeePerGas): ',
      eth_max_priority_fee, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_gasPrice" RPC Method  && Returns the current gas price in Wei.
eth_gasPrice = w3.eth.gas_price
print('\x1b[0;30;42meth_gasPrice\x1b[0m(eth_gasPrice): ',
      eth_gasPrice, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_accounts" RPC Method && Returns the list of known accounts.
eth_accounts = w3.eth.accounts
print('\x1b[0;30;42meth_accounts\x1b[0m: ', eth_accounts, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_blockNumber" RPC Method && Returns the number of the most recent block
eth_blockNumber = w3.eth.blockNumber
eth_get_block_number = w3.eth.get_block_number()
print('\x1b[0;30;42meth_blockNumber\x1b[0m(eth_blockNumber): ', eth_blockNumber)
print('\x1b[0;30;42meth_get_block_number\x1b[0m(eth_blockNumber): ',
      eth_get_block_number, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_protocolVersion" RPC Method  && Returns the id of the current Ethereum protocol version.
# eth_protocolVersion = w3.eth.protocolVersion
# print('\x1b[0;30;42meth_protocolVersion\x1b[0m(eth_protocolVersion): ', eth_protocolVersion , end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_chainId" RPC Method && Returns an integer value for the currently configured “Chain Id” value introduced in EIP-155. Returns None if no Chain Id is available.
eth_chainId = w3.eth.chain_id
print('\x1b[0;30;42meth_chainId\x1b[0m(eth_chainId): ',
      eth_chainId, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
print(
    f"\n{'*'*75}\n\t\t\t\x1b[0:30;41mWeb3 Methods\x1b[0m", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getBalance" RPC Method && Returns the balance of the given account at the block specified by block_identifier. account may be a checksum address or an ENS name
# Eth.get_balance(account, block_identifier=eth.default_block)
eth_getBalance = w3.eth.get_balance(
    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601")
print('\x1b[0;30;42meth_getBalance\x1b[0m(eth_getBalance): ',
      eth_getBalance, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getStorageAt" RPC Method && Returns the value from a storage position for the given account at the block specified by block_identifier. account may be a checksum address or an ENS name
# Eth.get_storage_at(account, position, block_identifier=eth.default_block)
eth_getStorageAt = w3.eth.getStorageAt(
    '0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B', 0)
print('\x1b[0;30;42meth_getStorageAt\x1b[0m: ',
      eth_getStorageAt, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getProof" RPC Method && Returns the values from an array of storage positions for the given account at the block specified by block_identifier. account may be a checksum address or an ENS name
# Eth.get_proof(account, positions, block_identifier=eth.default_block)
eth_getProof = w3.eth.get_proof(
    '0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B', [0])
print('\x1b[0;30;42meth_getProof\x1b[0m: ',
      f"'address':{eth_getProof['address']}, ...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getCode" RPC Method && Returns the bytecode for the given account at the block specified by block_identifier.
# Eth.get_code(account, block_identifier=eth.default_block)
eth_getCode = w3.eth.get_code("0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B")
print('\x1b[0;30;42meth_getCode\x1b[0m: ',
      f"{eth_getCode[:50]}...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getBlockByNumber" or "eth_getBlockByHash" RPC Methods && Returns the block specified by block_identifier. Delegates to "eth_getBlockByNumber" if block_identifier is an integer or one of the predefined block parameters 'latest', 'earliest', 'pending', otherwise delegates to eth_getBlockByHash. Throws BlockNotFound error if the block is not found.If full_transactions is True then the 'transactions' key will contain full transactions objects. Otherwise it will be an array of transaction hashes.
# Eth.get_block(block_identifier=eth.default_block, full_transactions=False)
eth_get_block = w3.eth.get_block(1000000)
print('\x1b[0;30;42meth_get_block\x1b[0m(eth_getBlockByNumber,eth_getBlockByHash): ',
      f"'difficulty': {eth_get_block['difficulty']}...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getBlockTransactionCountByNumber" or "eth_getBlockTransactionCountByHash" RPC Methods && Returns the number of transactions in the block specified by block_identifier. Delegates to "eth_getBlockTransactionCountByNumber" if block_identifier is an integer or one of the predefined block parameters 'latest', 'earliest', 'pending', otherwise delegates to "eth_getBlockTransactionCountByHash". Throws BlockNotFoundError if transactions are not found.
# Eth.get_block_transaction_count(block_identifier)
# eth_get_block_transaction_count = w3.eth.get_block_transaction_count(46147) # or
eth_get_block_transaction_count = w3.eth.get_block_transaction_count(
    "0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd")
print('\x1b[0;30;42meth_get_block_transaction_count\x1b[0m(eth_getBlockTransactionCountByNumber,eth_getBlockTransactionCountByHash): ',
      eth_get_block_transaction_count, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Method to get an Uncle from its hash is not available through RPC, a possible substitute is the method Eth.get_uncle_by_block
# Eth.getUncle(block_identifier)
# eth_getUncle = w3.eth.getUncle("0x685b2226cbf6e1f890211010aa192bf16f0a0cba9534264a033b023d7367b845")
eth_get_uncle_by_block = w3.eth.get_uncle_by_block(56160, 0)
print('\x1b[0;30;42meth_get_uncle_by_block\x1b[0m: ',
      f"'difficulty:'{eth_get_uncle_by_block['difficulty']}...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getUncleCountByBlockHash" or "eth_getUncleCountByBlockNumber" RPC methods && Returns the (integer) number of uncles associated with the block specified by block_identifier. Delegates to eth_getUncleCountByBlockNumber if block_identifier is an integer or one of the predefined block parameters 'latest', 'earliest', 'pending', otherwise delegates to eth_getUncleCountByBlockHash. Throws BlockNotFound if the block is not found.
# Eth.get_uncle_count(block_identifier)
# eth_get_uncle_count = w3.eth.get_uncle_count("0x685b2226cbf6e1f890211010aa192bf16f0a0cba9534264a033b023d7367b845") # or
eth_get_uncle_count = w3.eth.get_uncle_count(56160)
print('\x1b[0;30;42meth_get_uncle_count\x1b[0m(eth_getUncleCountByBlockHash,eth_getUncleCountByBlockNumber): ',
      eth_get_uncle_count, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getTransactionByHash" RPC Method && Returns the transaction specified by transaction_hash. If the transaction has not yet been mined throws web3.exceptions.TransactionNotFound.
# Eth.get_transaction(transaction_hash)
eth_get_transaction = w3.eth.get_transaction(
    "0xcefd3f0c97e67e89859f3fa63d95fda890fd78d897b5ccf2881410a4833a7e3b")
print('\x1b[0;30;42meth_get_transaction\x1b[0m(eth_getTransactionByHash): ',
      f"'blockHash': {dict(eth_get_transaction)['blockHash']}...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to eth_getRawTransactionByHash RPC Method && Returns the raw form of transaction specified by transaction_hash.If no transaction is found, TransactionNotFound is raised.
# Eth.get_raw_transaction(transaction_hash)
eth_get_raw_transaction = w3.eth.get_raw_transaction(
    "0xcefd3f0c97e67e89859f3fa63d95fda890fd78d897b5ccf2881410a4833a7e3b")
print('\x1b[0;30;42meth_get_raw_transaction\x1b[0m(eth_getRawTransactionByHash): ',
      eth_get_raw_transaction, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getTransactionByBlockNumberAndIndex" or "eth_getTransactionByBlockHashAndIndex" RPC Methods && Returns the transaction at the index specified by transaction_index from the block specified by block_identifier. Delegates to eth_getTransactionByBlockNumberAndIndex if block_identifier is an integer or one of the predefined block parameters 'latest', 'earliest', 'pending', otherwise delegates to eth_getTransactionByBlockHashAndIndex. If a transaction is not found at specified arguments, throws web3.exceptions.TransactionNotFound.
# Eth.get_transaction_by_block(block_identifier, transaction_index)
eth_get_transaction_by_block = w3.eth.get_transaction_by_block(
    "0x5c4030389c9079bef0fa816e9fca798ed42bfd3c8d1aa9ee5a73f6dc091e6bea", 1)
print('\x1b[0;30;42meth_get_transaction_by_block\x1b[0m\n(eth_getTransactionByBlockNumberAndIndex,eth_getTransactionByBlockHashAndIndex): ',
      f"'value': {eth_get_transaction_by_block['value']}...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Waits for the transaction specified by transaction_hash to be included in a block, then returns its transaction receipt. && Optionally, specify a timeout in seconds. If timeout elapses before the transaction is added to a block, then wait_for_transaction_receipt() raises a web3.exceptions.TimeExhausted exception.
# Eth.wait_for_transaction_receipt(transaction_hash, timeout=120, poll_latency=0.1)
eth_wait_for_transaction_receipt = w3.eth.wait_for_transaction_receipt(
    "0x93c7795d76f9e32388bfcff6b80d2f68c3cd8fd8c882d04d40c3579724026522")
print('\x1b[0;30;42meth_wait_for_transaction_receipt\x1b[0m: ',
      f"'blockNumber': {eth_wait_for_transaction_receipt['blockNumber']} ...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getTransactionReceipt" RPC Method && Returns the transaction receipt specified by transaction_hash. If the transaction has not yet been mined throws web3.exceptions.TransactionNotFound.If status in response equals 1 the transaction was successful. If it is equals 0 the transaction was reverted by EVM.
# Eth.get_transaction_receipt(transaction_hash)
eth_get_transaction_receipt = w3.eth.get_transaction_receipt(
    "0xcefd3f0c97e67e89859f3fa63d95fda890fd78d897b5ccf2881410a4833a7e3b")
print('\x1b[0;30;42meth_get_transaction_receipt\x1b[0m(eth_getTransactionReceipt): ',
      f"'blockNumber': {eth_get_transaction_receipt['blockNumber']} ...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getTransactionCount" RPC Method && Returns the number of transactions that have been sent from account as of the block specified by block_identifier.account may be a checksum address or an ENS name
# Eth.get_transaction_count(account, block_identifier=web3.eth.default_block)
eth_get_transaction_count = w3.eth.get_transaction_count(
    account='0xd3CdA913deB6f67967B99D67aCDFa1712C293601', block_identifier=eth_default_block)
print('\x1b[0;30;42meth_get_transaction_count\x1b[0m(eth_getTransactionCount): ',
      eth_get_transaction_count, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_sendTransaction" RPC Method
# Signs and sends the given transaction The transaction parameter should be a dictionary with the following fields.
# from: bytes or text, checksum address or ENS name - (optional, default: web3.eth.defaultAccount) The address the transaction is sent from.to: bytes or text,
# checksum address or ENS name - (optional when creating new contract) The address the transaction is directed to.gas: integer - (optional) Integer of the gas provided for the transaction execution.
# It will return unused gas.maxFeePerGas: integer or hex - (optional) maximum amount you’re willing to pay, inclusive of baseFeePerGas and maxPriorityFeePerGas.
# The difference between maxFeePerGas and baseFeePerGas + maxPriorityFeePerGas is refunded to the user.maxPriorityFeePerGas: integer or hex - (optional) the part of the fee that goes to the minergasPrice: integer - Integer of the gasPrice used for each paid gas LEGACY - unless you have a good reason to use gasPrice,
# use maxFeePerGas and maxPriorityFeePerGas instead.value: integer - (optional) Integer of the value send with this transactiondata: bytes or text - The compiled code of a contract OR the hash of the invoked method signature and encoded parameters. For details see Ethereum Contract ABI.nonce: integer - (optional) Integer of a nonce.
# This allows to overwrite your own pending transactions that use the same nonce.If the transaction specifies a data value but does not specify gas then the gas value will be populated using the estimate_gas() function with an additional buffer of 100000 gas up to the gasLimit of the latest block.
# In the event that the value returned by estimate_gas() method is greater than the gasLimit a ValueError will be raised.
# Eth.send_transaction(transaction)

# simple example (Web3.py and / or client determines gas and fees, typically defaults to a dynamic fee transaction post London fork)
# eth_send_transaction = w3.eth.send_transaction({
#   'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#   'from': w3.eth.coinbase,
#   'value': 12345
# })
# ## Dynamic fee transaction, introduced by EIP-1559:
# eth_send_transaction = w3.eth.send_transaction({
#   'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#   'from': w3.eth.coinbase,
#   'value': 12345,
#   'gas': 21000,
#   'maxFeePerGas': w3.toWei(250, 'gwei'),
#   'maxPriorityFeePerGas': w3.toWei(2, 'gwei'),
# })
# ## Legacy transaction (less efficient)
# eth_send_transaction = w3.eth.send_transaction({
#   'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#   'from': w3.eth.coinbase,
#   'value': 12345,
#   'gas': 21000,
#   'gasPrice': w3.toWei(50, 'gwei'),
# })
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_signTransaction" RPC Method.
# Returns a transaction that’s been signed by the node’s private key, but not yet submitted. The signed tx can be submitted with Eth.send_raw_transaction
# Eth.sign_transaction(transaction)
# eth_sign_transaction = w3.eth.sign_transaction(dict(
#     nonce=w3.eth.get_transaction_count(w3.eth.coinbase),
#     maxFeePerGas=2000000000,
#     maxPriorityFeePerGas=1000000000,
#     gas=100000,
#     to='0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#     value=1,
#     data=b'',
#     )
# )
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_call" RPC Method && Executes the given transaction locally without creating a new transaction on the blockchain. Returns the return value of the executed contract.The transaction parameter is handled in the same manner as the send_transaction() method.
# Eth.call(transaction, block_identifier=web3.eth.default_block, state_override=None)
# eth_call = w3.eth.call({'value': 0, 'gas': 21736, 'maxFeePerGas': 2000000000, 'maxPriorityFeePerGas': 1000000000,
#                        'to': '0xc305c901078781C232A2a521C2aF7980f8385ee9', 'data': '0x477a5c98'},block_identifier=300)
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_feeHistory" RPC Method
# ######Parameters
# "block_count" (int or hexstring) – The number of blocks in the requested range. Depending on the client, this value should be either a int between 1 and 1024 or a hexstring. Less than requested may be returned if not all blocks are available.
# "newest_block" (int or BlockParams) – The newest, highest-numbered, block in the requested range. This value may be an int or one of the predefined block parameters 'latest', 'earliest', or 'pending'.
# "reward_percentiles" (List[float] or None) – (optional) A monotonically increasing list of percentile float values to sample from each block’s effective priority fees per gas in ascending order, weighted by gas used.
# ######Returns
# An AttributeDict containing the following keys:
# oldestBlock (int) – The oldest, lowest-numbered, block in the range requested as a BlockNumber type with int value.
# baseFeePerGas (List[Wei]) – An array of block base fees per gas. This includes the next block after the newest of the returned range, because this value can be derived from the newest block. Zeroes are returned for pre-EIP-1559 blocks.
# gasUsedRatio (List[float]) – An array of gasUsed/gasLimit float values for the requested blocks.
# reward (List[List[Wei]]) – (optional) A two-dimensional array of effective priority fees per gas at the requested block percentiles.
eth_fee_history = w3.eth.fee_history(1, 'latest', [10, 90])
print('\x1b[0;30;42meth_fee_history\x1b[0m(eth_feeHistory): ',
      f"'oldestBlock': {eth_fee_history['oldestBlock']},'reward':{eth_fee_history['reward']} ...", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
print(
    f"\n{'*'*75}\n\t\t\t\x1b[0:30;41mWeb3 Filters\x1b[0m", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_newFilter", "eth_newBlockFilter", and "eth_newPendingTransactionFilter" RPC Methods.
# This method delegates to one of three RPC methods depending on the value of filter_params.
# If filter_params is the string 'pending' then a new filter is registered using the eth_newPendingTransactionFilter RPC method. This will create a new filter that will be called for each new unmined transaction that the node receives.
# If filter_params is the string 'latest' then a new filter is registered using the eth_newBlockFilter RPC method. This will create a new filter that will be called each time the node receives a new block.
# If filter_params is a dictionary then a new filter is registered using the eth_newFilter RPC method. This will create a new filter that will be called for all log entries that match the provided filter_params.
# This method returns a web3.utils.filters.Filter object which can then be used to either directly fetch the results of the filter or to register callbacks which will be called with each result of the filter.
# When creating a new log filter, the filter_params should be a dictionary with the following keys.
# fromBlock: integer/tag - (optional, default: “latest”) Integer block number, or “latest” for the last mined block or “pending”, “earliest” for not yet mined transactions.
# toBlock: integer/tag - (optional, default: “latest”) Integer block number, or “latest” for the last mined block or “pending”, “earliest” for not yet mined transactions.
# address: string or list of strings, each 20 Bytes - (optional) Contract address or a list of addresses from which logs should originate.
# topics: list of 32 byte strings or null - (optional) Array of topics that should be used for filtering. Topics are order-dependent. This parameter can also be a list of topic lists in which case filtering will match any of the provided topic arrays.
# Eth.filter(filter_params)
eth_filter_latest = w3.eth.filter('latest')
eth_filter_pending = w3.eth.filter('latest')
eth_filter_fromBlock_toBlock = w3.eth.filter(
    {'fromBlock': 1000000, 'toBlock': 1000100, 'address': '0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B'})
print('\x1b[0;30;42meth_filter_latest\x1b[0m(eth_newFilter,eth_newBlockFilter): ', eth_filter_latest)
print('\x1b[0;30;42meth_filter_pending\x1b[0m(eth_newPendingTransactionFilter): ',
      eth_filter_pending)
print('\x1b[0;30;42meth_filter_fromBlock_toBlock\x1b[0m: ',
      eth_filter_fromBlock_toBlock, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# Delegates to "eth_getFilterChanges" RPC Method && Returns all new entries which occurred since the last call to this method for the given filter_id
# Eth.get_filter_changes(self, filter_id)
# filter_ = w3.eth.filter()
# eth_get_filter_changes = w3.eth.get_filter_logs(filter_.filter__id)
# print('\x1b[0;30;42meth_get_filter_changes\x1b[0m: ', eth_get_filter_changes , end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
print(
    f"\n{'*'*75}\n\t\t\t\x1b[0:30;41mWeb3 Contracts\x1b[0m", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
# If address is provided, then this method will return an instance of the contract defined by abi. The address may be a checksum string, or an ENS name like 'mycontract.eth'.
# Eth.contract(address=None, contract_name=None, ContractFactoryClass=Contract, **contract_factory_kwargs)
contract = w3.eth.contract()
print('\x1b[0;30;42mcontract\x1b[0m: ', contract, end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
print(
    f"\n{'*'*75}\n\t\t\t\x1b[0:30;41mWeb3 Convertors\x1b[0m", end=f"\n{'*'*75}\n")
# ********************************************************************************************************************************************************************************************
print("""
 Web3.toHex
 Web3.toInt
 Web3.toJson
 Web3.toText
      """, end=f"\n{'*'*75}\n")
# web3 convertors
# Web3.toHex
# Web3.toInt
# Web3.toJson
# Web3.toText
