from flask_restful import Resource
from extractor import api
from extractor.resources import *

api.add_resource(Extractor, '/')
api.add_resource(Status, '/<string:rid>')

