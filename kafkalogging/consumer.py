from kafka import KafkaConsumer
consumer = KafkaConsumer('int')
for message in consumer:
    print (message)