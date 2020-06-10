from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


# Creates Flask app
app = Flask(__name__)
app.secret_key = 'cesar'
# Creates API for app
api = Api(app)

# Allows authentification of users
jwt = JWT(app, authenticate, identity)

items = []

# Defines Resource
class Item(Resource):
    @jwt_required()
    # Defines the methods that the resource accepts
    def get(self,name):
        # lambda function used to filter through list
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with '{}' already exists.".format(name)}, 400
        # get JSON payload from request
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {"items": items}

# Adss resource and determines how it's accesed
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)
