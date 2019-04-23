from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('int', b'Test')
producer.send('int', key=b'message-two', value=b'This is Test with key')