from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name': 'my items',
                'price': 15000
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
            return jsonify({'msg': 'store is not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'msg': 'store is not found'})


@app.route('/store/<string:name>/item')
def create_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
            return jsonify({'msg': 'store is not found'})


app.run()
