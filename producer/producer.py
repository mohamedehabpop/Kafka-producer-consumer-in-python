from kafka import KafkaProducer
import time

kafka_host = 'localhost:9092'
topic = 'fancy-topic'

producer = KafkaProducer(bootstrap_servers=[kafka_host],
                         value_serializer=lambda x: x.encode('utf-8'))

i = 0
while True:
    message = f"message #{i}"
    key = str(i).encode('utf-8')
    producer.send(topic, key=key, value=message)
    print(f"Sent message: {message}")
    i += 1
    time.sleep(1)