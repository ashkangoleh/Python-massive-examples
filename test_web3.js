const Web3 = require("web3");
// https://web3js.readthedocs.io/en/v1.7.0/
try {
    const rpcUrl = "http://168.119.0.182:8545";
    const web3 = new Web3(rpcUrl);

    web3.eth.getBlockNumber().then(console.log);
} catch (e) {
    console.log(e);;
}