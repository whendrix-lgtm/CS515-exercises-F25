from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

students = {1 : {"name":"Alice", "class":"junior"}, 2 : {"name":"Bob", "class":"sophomore"}}

student_parser = reqparse.RequestParser()
student_parser.add_argument('name', str)
student_parser.add_argument('class', str)

action_parser = reqparse.RequestParser()
action_parser.add_argument('action', str)

def validate_class(str):
  if str in ['freshman', 'sophomore', 'junior', 'senior']:
    return True
  elif str == '':
    abort(400, message='missing class')
  else:
    abort(400, message='illegal class designation')

class Directory (Resource):
  def get(self):
    return students
  def post(self):
    data = student_parser.parse_args()
    validate_class(data['class'])
    newid = max(students.keys())+1
    students[newid] = data
    return students[newid]

class Student (Resource):
  def get(self, id):
    return students[id]
  def post(self, id):
    data = student_parser.parse_args()
    validate_class(data['class'])
    students[id] = data
    return data
  def delete(self, id):
    # TODO:  check id in students
    del students[id]
    return 'Success', 200
  def put(self, id):
    action = action_parser.parse_args()
    if action['action'] == 'advance':
      self.advance(id)
  def advance(self, id):
    if students[id]['class'] == 'freshman':
      students[id]['class'] = 'sophomore'
    elif students[id]['class'] == 'sophomore':
      students[id]['class'] = 'junior'
    elif students[id]['class'] == 'junior':
      students[id]['class'] = 'senior'
    elif students[id]['class'] == 'senior':
      del students[id]

api.add_resource(Directory, '/students')
api.add_resource(Student, '/student/<int:id>')

