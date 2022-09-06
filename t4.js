// class LRUCache {
//     constructor(capacity) {
//         this.cache = new Map();
//         this.capacity = capacity;
//     }

//     get(key) {
//         if (!this.cache.has(key)) return -1;

//         let val = this.cache.get(key);

//         this.cache.delete(key);
//         this.cache.set(key, val);

//         return val;
//     }

//     put(key, value) {
//         this.cache.delete(key);

//         if (this.cache.size === this.capacity) {
//             this.cache.delete(this.cache.keys().next().value);
//             this.cache.set(key, value);
//         } else {
//             this.cache.set(key, value);
//         }
//     }

//     // Implement LRU/MRU retrieval methods
//     getLeastRecent() {
//         return Array.from(this.cache)[0];
//     }

//     getMostRecent() {
//         return Array.from(this.cache)[this.cache.size - 1];
//     }

// }

// function fib(n) {
//     if (n < 2) {
//         return n
//     }
//     return fib(n - 1) + fib(n - 2)
// }

// const lru = new LRUCache(fib(30))

const { Kafka } = require("kafkajs");

const kafka = new Kafka({
    clientId: "test1",
    brokers: ["arz.local:9093"],
});
const consumer = kafka.consumer({
    groupId: "test318424",
});

const run = async() => {
    // Consuming
    await consumer.connect();
    await consumer.subscribe({ topic: "OHLCVs", fromBeginning: true });
    try {
        await consumer.run({
            eachMessage: async({ topic, partition, message }) => {
                // console.log({
                //     value: (typeof message.value.toString())
                // });
                const msg = message.value.toString();
                const parsed_msg = JSON.parse(msg);
                console.log(parsed_msg);
                parsed_msg["candles"].pop();
                console.table(parsed_msg["candles"].pop());
            },
        });
    } catch (error) {
        await consumer.disconnect();
    }
};

run().catch(console.error);

// var Kafka = require("node-rdkafka");
// let fs = require("fs");

// const pem = fs.readFileSync("/home/ashkan/Videos/ca_crt.pem", "utf-8");

// var consumer = new Kafka.KafkaConsumer({
//     "group.id": "test_gid",
//     "metadata.broker.list": "arz.local:9093,",
// 'enable.auto.commit': false,
// 'ssl.certificate.pem':pem,
// 'security.protocol': 'SSL',
// 'metadata.broker.list': 'kafka.zebra.arz.team:10192, kafka.lion.arz.team:10191, kafka.hippo.arz.team:10193',
// 'enable.auto.commit': false,
// 'ssl.certificate.pem':pem,
// 'security.protocol': 'SSL',
// });

// consumer
//     .on("ready", function () {
//         consumer.subscribe(["kline.5m.binance"]);
//         consumer.consume();
//     })
//     .on("data", function (data) {
//         if (!data) {
//             console.log(data.value.toString());
//         } else {
//             console.log("data is null");
//         }
//     });