"""
Http Server for our API
"""

from flask import Flask, jsonify, request

from controller import product_controller

app = Flask(__name__)


def serialize(products):
    return list(
        map(
            lambda p: p.serialize(), products
        )
    )


@app.route("/product/<name>")
def get_product(name: str):
    return jsonify(
        {"product": product_controller.get_by_name(name).serialize()}
    )


@app.route("/products")
def get_all_products():
    return jsonify(
        {"products": serialize(product_controller.get())}
    )


@app.route("/product", methods=['POST'])
def insert_product():
    name = request.json.get('name')
    desc = request.json.get('desc')
    value = float(request.json.get('value'))

    p = product_controller.save(name, desc, value)
    return jsonify(
        {"product": p.serialize()}
    )


@app.route("/update_product/<p_name>", methods=['PUT'])
def update_product(p_name: str):
    name = request.json.get("name")
    desc = request.json.get("desc")
    value = request.json.get("value")

    return jsonify(
        {"product": product_controller.change(p_name, name=name, desc=desc, value=value).serialize()}
    )


@app.route('/delete_product/<name>', methods=['DELETE'])
def delete_product(name: str):
    return jsonify(
        {"product_deleted": product_controller.delete_by_id(id).serialize()}
    )


if __name__ == '__main__':
    app.run()
