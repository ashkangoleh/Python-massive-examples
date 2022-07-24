import time
import ray
from config import kafka
from producer import get_palette, producer

@ray.remote(num_cpus=2)
class RayConsumer(object):
    def __init__(self, kafka, source):
        from confluent_kafka import Consumer
        self.c = Consumer({**kafka['connection'], **kafka['consumer']})
        self.c.subscribe([source])


    def start(self):
        self.run = True
        while self.run:
            msg = self.c.poll(0.1)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            ray.get(get_palette.remote(msg.value()))


    def stop(self):
        self.run = False


    def destroy(self):
        self.c.close()
        
def main(topic):
    n_consumers= 1
    consumers = [RayConsumer.remote(kafka, topic) for _ in range(n_consumers)]

    try:
        refs = [c.start.remote() for c in consumers]
        ray.get(refs)
    except KeyboardInterrupt:
        for c in consumers:
            c.stop.remote()
    finally:
        for c in consumers:
            c.destroy.remote()
        producer.destroy.remote()
        ray.kill(producer)
        
main('kline.latest.n.dev.binance.5')