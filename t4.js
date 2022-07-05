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
var Kafka = require('node-rdkafka');
var consumer = new Kafka.KafkaConsumer({
    'group.id': 'Foo',
    'metadata.broker.list': 'arz.local:9093',
    'offset_commit_cb': function(err, topicPartitions) {
      if (err) {
        console.error(err);
      } else {
        console.log(topicPartitions);
      }
    }
  })

console.log(consumer.connect());
consumer
  .on('ready', function() {
    consumer.subscribe(['test']);
    consumer.consume();
  })
  .on('data', function(data) {
    console.log(data.value.toString());
  });