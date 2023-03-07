"""
Confluent connector
"""
from confluent_kafka import Consumer, KafkaError
import json

# Set up Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

# Set up Kafka consumer
consumer = Consumer(conf)
consumer.subscribe(['my_topic'])

# Find the last committed offset
committed_offsets = consumer.committed(consumer.assignment())
if committed_offsets:
    last_committed_offset = committed_offsets[0].offset()
else:
    last_committed_offset = None

# Seek to the last committed offset
if last_committed_offset is not None:
    consumer.seek(consumer.assignment()[0], last_committed_offset)

# Consume messages from Kafka
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            print(f"Reached end of partition for {message.topic()}/{message.partition()}")
        else:
            print(f"Error while consuming from {message.topic()}/{message.partition()}: {message.error()}")
    else:
        # Process the message
        print(f"Received message: {json.loads(message.value())}")

        # Manually commit the offset for the processed message
        consumer.commit({
            'topic': message.topic(),
            'partition': message.partition(),
            'offset': message.offset()
        })

"""
kafka connector
"""

from kafka import KafkaConsumer
import json

# Set up Kafka consumer
consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    enable_auto_commit=False,  # Disable auto-commit to allow manual offset management
    group_id='my-group'
)

# Find the last committed offset
committed_offsets = consumer.committed(consumer.assignment())
if committed_offsets:
    last_committed_offset = committed_offsets[0].offset
else:
    last_committed_offset = None

# Seek to the last committed offset
if last_committed_offset is not None:
    consumer.seek(consumer.assignment()[0], last_committed_offset)

# Consume messages from Kafka
for message in consumer:
    # Process the message
    print(f"Received message: {message.value}")

    # Manually commit the offset for the processed message
    consumer.commit()


"""
last offset with seek() if offset wasnt commited starting from beginning of partition
"""
from confluent_kafka import Consumer, KafkaError

# Set up Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'enable.auto.commit': False
}

# Set up Kafka consumer
consumer = Consumer(conf)
consumer.subscribe(['my_topic'])

# Get the last committed offset for the consumer group
committed_offsets = consumer.committed(consumer.assignment())
if committed_offsets:
    last_committed_offset = committed_offsets[0].offset
    consumer.seek(consumer.assignment()[0], last_committed_offset)
else:
    consumer.seek_to_beginning(consumer.assignment())

# Consume messages from Kafka starting from the last committed offset
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            print(f"Reached end of partition for {message.topic()}/{message.partition()}")
        else:
            print(f"Error while consuming from {message.topic()}/{message.partition()}: {message.error()}")
    else:
        # Process the message
        print(f"Received message: {message.value()}")

        # Manually commit the offset for the processed message
        consumer.commit({
            'topic': message.topic(),
            'partition': message.partition(),
            'offset': message.offset()
        })

"""
last offset with seek() if offset wasnt commited starting from beginning of partitions (all partitions)
"""
from confluent_kafka import Consumer, KafkaError

# Set up Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'enable.auto.commit': False
}

# Set up Kafka consumer
consumer = Consumer(conf)
consumer.subscribe(['my_topic'])

# Get the last committed offset for each partition in the consumer group
committed_offsets = consumer.committed(consumer.assignment())
for partition in committed_offsets:
    if partition:
        last_committed_offset = partition.offset
        consumer.seek(partition, last_committed_offset)
    else:
        consumer.seek_to_beginning(partition)

# Consume messages from Kafka starting from the last committed offset
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            print(f"Reached end of partition for {message.topic()}/{message.partition()}")
        else:
            print(f"Error while consuming from {message.topic()}/{message.partition()}: {message.error()}")
    else:
        # Process the message
        print(f"Received message: {message.value()}")

        # Manually commit the offset for the processed message
        consumer.commit({
            'topic': message.topic(),
            'partition': message.partition(),
            'offset': message.offset()
        })
