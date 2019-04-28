from flask_restful import Resource
from main import api
from main.resources import *

api.add_resource(Extractor, '/')
api.add_resource(Status, '/status')

