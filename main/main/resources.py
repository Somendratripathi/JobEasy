from flask import request
from flask_restful import Resource
from main import status_dict

import uuid
import json

class Extractor(Resource):
    def post(self):
        try:
            #html = request.data.decode('utf-8')
            #print(html)
            uid = str(uuid.uuid4())
            status_dict[uid] = 'PENDING'
            print("FROM GET: ", status_dict)
            '''
            write html document and uid to kafka:

            kafka.write(topic, json.dumps({
                "uid": uid,
                "html": html
            })
            '''
            
        except Exception as e:
            print(e)
            return {"error": e}, 400
        return uid #anything representing some resource id

class Status(Resource):
    def get(self):
        print("FROM POST:", status_dict)
        uid = request.args.get('uid')
        if uid == None:
            return {"error": "must include 'uid' query string parameter"}, 400

        status = status_dict.get(uid)

        if status == None:
            return {"error": "uid not found"}, 404
        
        return {"status": status}, 200

    def post(self):
        uid, status = request.args.get('uid'), request.args.get('status')
        if uid not in status_dict.keys():
            return {"error": "uid is not in status dictionary"}, 400
        
        status_dict[uid] = status
        return 200
    
    def delete(self):
        uid = request.args.get('uid')
        if uid in status_dict.keys():
            del status_dict[uid]
        return 200
