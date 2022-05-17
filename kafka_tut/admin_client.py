from kafka import KafkaAdminClient as kac
from kafka.admin import NewTopic


admin_client = kac(
    bootstrap_servers="localhost:9092",client_id="test"
)

topic_list = []

new_topic = NewTopic(name="t1",num_partitions=2,replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)


