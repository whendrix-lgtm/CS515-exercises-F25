from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

students = {1 : {"name":"Alice", "class":"junior"}, 2 : {"name":"Bob", "class":"sophomore"}}

student_parser = reqparse.RequestParser()
student_parser.add_argument('name', str)
student_parser.add_argument('class', str)

class Directory (Resource):
  def get(self):
    return students
  def post(self):
    data = student_parser.parse_args()
    # TODO:  data validation
    newid = max(students.keys())+1
    students[newid] = data
    return students[newid]


class Student (Resource):
  def get(self, id):
    return students[id]
  def post(self, id):
    data = student_parser.parse_args()
    # TODO:  add data checking here
    students[id] = data
    return data
  def delete(self, id):
    # TODO:  check id in students
    del students[id]
    return 'Success', 200

api.add_resource(Directory, '/students')
api.add_resource(Student, '/student/<int:id>')

