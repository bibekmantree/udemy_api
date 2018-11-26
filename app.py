from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
            {'name': 'sangeetha',
             'items':
                 [
                     {'name': 'redmi',
                      'price': 100},
                     {'name': 'iphone',
                      'price': 800},
                 ]
             },
            {'name': 'poorvika',
             'items':
                 [
                     {'name': 'oppo',
                      'price': 150},
                     {'name': 'vivo',
                      'price': 100},
                 ]
             }
        ]


@app.route('/')
def hello():
    return render_template('index.html')
# I am a server.
# POST: used to receive data
# GET is used to send data


# POST /store {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(request_data)


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    """Returns all store and it's data"""
    return jsonify({'stores': stores})


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "Store not found"})


# POST /store/<string:name>/item {item:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            store["items"].append(
                {
                    "name": request_data["name"],
                    "price": request_data["price"]
                }
            )
            return jsonify({"message": store})
    return jsonify({"message": "Store not found"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({name: store['items']})
    return jsonify({"message": "Store not found"})


# GET /store/<string:name>/item/<string:item> {name:}
@app.route('/store', methods=['GET'])
def get_by_item_in_store(name,item):
    pass


app.run(host='0.0.0.0', port=5000)
