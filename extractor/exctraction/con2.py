from kafka import KafkaConsumer,KafkaProducer
from time import sleep
from exctraction import Extraction
from bs4 import BeautifulSoup
import re
import json
from html import escape
from json import loads,dumps
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('clientstore')

kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode('utf-8'))

consumer1=KafkaConsumer('sample',bootstrap_servers=['localhost:9092'],value_deserializer=lambda x: loads(x.decode('utf-8')))

#consumer2= KafkaConsumer('btest')

for message in consumer1:
    print(message)
    company, jobtitle, jobdescription = Extraction.extract_text(message.value['html'])
    u=message.value['uid']
    print(u)
    print(company, jobtitle)
    kafka_producer.send('query', value={
        "company": company,
        "jobtitle": jobtitle,
        "jobdescription": jobdescription,
        "uid": u
    })
    CQLString = "INSERT INTO logs (uid) VALUES (%s)"
    session.execute(CQLString, (u,))
