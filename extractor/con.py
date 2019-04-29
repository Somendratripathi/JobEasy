from kafka import KafkaConsumer
from time import sleep
from exctraction import Extraction
from bs4 import BeautifulSoup
import re
import json
from html import escape
from json import loads

kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode('utf-8'))

consumer1=KafkaConsumer('sample',value_deserializer=lambda x: loads(x.decode('utf-8')))

#consumer2= KafkaConsumer('btest')

for message in consumer1:
    #print(html)
    #print(type(html))
    print(message)
    company, jobtitle, jobdescription = Extraction.extract_text(message.value)
    print(company, jobtitle)
    kafka_producer.send('query', value={
        "company": company,
        "jobtitle": jobtitle,
        "jobdescription": jobdescription
    })
