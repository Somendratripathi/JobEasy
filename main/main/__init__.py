from flask import Flask, request
from flask_restful import Resource, Api
from kafka import KafkaProducer
from json import dumps

app = Flask(__name__)
api = Api(app)

status_dict = {}
kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode('utf-8'))

from . import routes

