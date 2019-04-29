from kafka import KafkaConsumer
from time import sleep
from exctraction import Extraction
from bs4 import BeautifulSoup
import re
import json
from html import escape
from json import loads

consumer1=KafkaConsumer('sample',value_deserializer=lambda x: loads(x.decode('utf-8')))
#consumer2= KafkaConsumer('btest')

for message in consumer1:
    #print(html)
    #print(type(html))
    print(message)
    company, jobtitle, jobdescription =Extraction.extract_text(message.value)
    print(company, jobtitle)
