from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer('t1',bootstrap_servers=['localhost:9092'])
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value.decode('utf-8'))))