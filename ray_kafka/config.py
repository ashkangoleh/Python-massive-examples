import ray

KAFKA_SERVER = "arz.local:9093"

kafka = {
  'connection': {'bootstrap.servers': KAFKA_SERVER},
  'consumer': {
    'group.id': 'ray5',
    'enable.auto.commit': True,
    'auto.offset.reset': 'earliest'
  },
  'producer': {}
}

ray.init()