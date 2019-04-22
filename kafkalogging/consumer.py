from kafka import KafkaConsumer
consumer = KafkaConsumer('clientaccess')
for message in consumer:
    print (message)