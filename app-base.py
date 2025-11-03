from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = {1 : {"name":"Alice", "class":"junior"}, 2 : {"name":"Bob", "class":"sophomore"}}

