"""
Http Server for our API
"""
# TODO: Implement other endpoints
from flask import Flask, jsonify, request

from controller import product_controller

app = Flask(__name__)


@app.route("/product/<name>")
def get_product(name: str):
    return jsonify(
        product_controller.get_by_name(name).serialize()
    )


@app.route("/product", methods=['POST'])
def insert_product():
    name = request.data.get('name')
    desc = request.data.get('desc')
    value = float(request.data.get('value'))

    p = product_controller.save(name, desc, value)
    return jsonify(
        p.serialize()
    )
