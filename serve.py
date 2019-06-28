from flask import Flask, jsonify, json, request

port = 9999 # Change port variable as per need
debug = True # Change debug mode as per need

app = Flask(__name__)

products = [{ 'id': 1, 'name': 'Product 1'}, { 'id':2, 'name': 'Product 2' }, { 'id':3, 'name': 'Product 3' }]

@app.route('/api/products', methods=['GET'])
def list():
    return jsonify(products)

@app.route('/api/products/<int:id>', methods=['GET'])
def detail(id):
    filtered_products = [product for product in products if product['id'] == id]
    return jsonify({ 'product': filtered_products[0] })

@app.route('/api/products/', methods=['POST'])
def create():
    id = len(products) + 1
    name = request.json["name"]
    products.append({
        "id": id,
        "name": name
    })
    return jsonify(products)

@app.route('/api/products/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    filtered_products = [product for product in products if product['id'] == id]
    filtered_products[0]['name'] = request.json["name"]

    return jsonify(filtered_products)

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete(id):
    filtered_products = [product for product in products if product['id'] == id]
    products.remove(filtered_products[0])

    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=debug, port=port)

