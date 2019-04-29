from flask import request
from flask_restful import Resource
from kafka import KafkaProducer
import json
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

class Extractor(Resource):
    def post(self):
        try:
            html = request.data.decode('utf-8')
            print(type(html))
            #html=json.dumps(html)
            producer.send('sample', value=html)
             
        except Exception as e:
            print(e)
            return {"error": e}, 400
        return 55 #anything representing some resource id

class Status(Resource):
    def get(self, rid):
        pass

