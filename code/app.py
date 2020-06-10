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
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self,name):
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
