from flask import Flask, request
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
        # lambda function used to filter through list
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if the item else 404

    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with '{}' already exists.".format(name)}, 400
        # get JSON payload from request
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items": items}

# Adss resource and determines how it's accesed
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)
