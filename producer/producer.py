
# from time import sleep
# from json import dumps
# from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda m: dumps(m).encode('ascii'))

# for e in range(1000):
#     data = {'number' : e}
#     print(data)
#     producer.send('test', value=data)
#     sleep(1)

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