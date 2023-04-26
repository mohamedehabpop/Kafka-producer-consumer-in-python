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