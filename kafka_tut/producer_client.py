from kafka import KafkaProducer
import json
from data import get_registered_user
import time
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=["localhost:9093"],value_serializer=json_serializer)
producer2 = KafkaProducer(bootstrap_servers=["localhost:9093"],value_serializer=json_serializer)


if __name__ == '__main__':
    while 1==1:
        registered_user = get_registered_user()
        registered_user2 = get_registered_user()
        print(registered_user)
        producer.send('t2',registered_user)
        producer2.send('t2',registered_user2)
        time.sleep(1)
