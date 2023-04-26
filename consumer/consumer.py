# from kafka import KafkaConsumer
# from json import loads

# consumer = KafkaConsumer(
#     'test',
#      bootstrap_servers=['localhost:9092'],
#      value_deserializer=lambda m: loads(m.decode('ascii')))

# for message in consumer:
#     print(message)
#     message = message.value
#     print('{} found'.format(message))

from kafka import KafkaConsumer

kafka_host = 'localhost:9092'
topic = 'fancy-topic'

consumer = KafkaConsumer(topic,
                         bootstrap_servers=[kafka_host],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda x: x.decode('utf-8'))

for message in consumer:
    print(f"Received message: {message.value}")