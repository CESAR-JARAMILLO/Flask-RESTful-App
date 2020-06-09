from flask import Flask
from flask_restful import Resource, Api


# Creates Flask app
app = Flask(__name__)
# Creates API for app
api = Api(app)

items = []

# Defines Resource
class Item(Resource):
    # Defines the methods that the resource accepts
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item

    def post(self,name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item

# Adss resource and determines how it's accesed
api.add_resource(Item, '/item/<string:name>')

app.run()
