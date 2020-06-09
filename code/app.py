from flask import Flask
from flask_restful import Resource, Api


# Creates Flask app
app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self,name):
        return {'student':name}

api.add_resource(Student, '/student/<string:name>')

app.run()
