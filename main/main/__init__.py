from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
status_dict = {}

from . import routes

