function format_time(s) {
    return new Date(s * 1e3).toISOString().slice(-13, -5);
}
const test_obj = {
    symbol: 'ETH-USDT',
    candles: [
        '1662365520',
        '1560.06',
        '1560.04',
        '1560.06',
        '1560.04',
        '3.2144777',
        '5014.778025818'
    ]
}
test_obj['candles'].pop()
const date = new Date(test_obj['candles'][0] * 1000)



console.log(format_time(test_obj['candles'][0]))
console.log(test_obj['candles'])