import ray
import json
from config import kafka

@ray.remote
class RayProducer:
    def __init__(self, kafka, sink):
        from confluent_kafka import Producer
        self.producer = Producer({**kafka['connection'], **kafka['producer']})
        self.sink = sink

    def produce(self, palette):
        self.producer.produce(self.sink, palette)
        self.producer.poll(0)

    def destroy(self):
        self.producer.flush(30)


producer = RayProducer.options(name='producer').remote(kafka, 'test')




@ray.remote(num_cpus=2)
def get_palette(msg_value):
  try:
    message = msg_value.decode('utf-8')
    producer = ray.get_actor('producer')
    ray.wait(producer.produce.remote(message))
  except Exception as e:
    print('Unable to process:', e)
