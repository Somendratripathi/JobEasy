from flask import request
from flask_restful import Resource

class Extractor(Resource):
    def post(self):
        try:
            html = request.data.decode('utf-8')
            print(html)
            # extraction code here 
        except Exception as e:
            print(e)
            return {"error": e}, 400
        return 55 #anything representing some resource id

class Status(Resource):
    def get(self, rid):
        pass

