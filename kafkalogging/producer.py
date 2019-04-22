from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='2181')
producer.send('clientaccess', b'Test')
producer.send('clientaccess', key=b'message-two', value=b'This is Test with key')