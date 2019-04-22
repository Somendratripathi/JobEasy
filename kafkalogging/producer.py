from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='2181')
producer.send('sample', b'Test')
producer.send('sample', key=b'message-two', value=b'This is Test with key')