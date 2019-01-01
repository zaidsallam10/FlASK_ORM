from flask import Flask, session, jsonify, abort, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:300/shopping_system_v1'
app.config['SQLALCHEMY_ECHO'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
mysql = MySQL(app)
db = SQLAlchemy(app)

marshmallow = Marshmallow(app)
from controller import UserController
from controller import ProductController
from controller import RequestController

# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/users', methods=['GET'])
def allUsers():
    return jsonify(UserController.UserController().getAllUsers())


@app.route('/vendors', methods=['GET'])
def allVendors():
    return jsonify(UserController.UserController().getAllVendors())


@app.route('/users/<id>')
def userById(id):
    return jsonify(UserController.UserController().getById(id=id))


@app.route('/signup', methods=['POST'])
def signUp():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().signUp(data))


@app.route('/login_user', methods=['POST'])
def loginUser():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().loginUser(data['email_address'], data['password']))


@app.route('/login_vendor', methods=['POST'])
def loginVendor():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().loginVendor(data['email_address'], data['password']))


@app.route('/login_admin', methods=['POST'])
def loginAdmin():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().loginAdmin(data['email_address'], data['password']))


@app.route('/products')
def getAllProducts():
    return jsonify(ProductController.ProductController().getAll())


@app.route('/products/<id>')
def getProductById(id):
    return jsonify(ProductController.ProductController().getById(id=id))


@app.route('/products/types')
def getProductTypes():
    return jsonify(ProductController.ProductController().getAllTypes())


@app.route('/')
def hi():
    return "Hello To Online Shopping System"


@app.route('/products/<id>', methods=['DELETE'])
def deleteProduct(id):
    return jsonify(ProductController.ProductController().deleteProduct(id))


@app.route('/users/<id>/hold', methods=['PUT'])
def holdUser(id):
    return jsonify(UserController.UserController().holdAccount(id))


@app.route('/users/<id>/un_hold', methods=['PUT'])
def unHoldUser(id):
    return jsonify(UserController.UserController().unHoldAccount(id))


@app.route('/users/holded')
def holdedAccounts():
    return jsonify(UserController.UserController().holdedAccounts())


@app.route('/products', methods=['POST'])
def addProduct():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(ProductController.ProductController().addProduct(data))


@app.route('/products/<id>', methods=['PUT'])
def updateProduct(id):
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(ProductController.ProductController().updateProduct(id, data))


# getMyProducts
@app.route('/users/<id>/products', methods=['GET'])
def getMyProducts(id):
    return jsonify(UserController.UserController().getMyProducts(id))


# getCustomerRequests
@app.route('/users/<id>/requests', methods=['GET'])
def getCustomerRequests(id):
    return jsonify(RequestController.RequestController().getCustomerRequests(id))


@app.route('/users/<id>/closed_requests', methods=['GET'])
def getCustomerClosedRequests(id):
    return jsonify(RequestController.RequestController().getCustomerClosedRequests(id))


# getCustomerClosedRequests


# getVendorRequests
@app.route('/users/<id>/orders', methods=['GET'])
def getVendorRequests(id):
    return jsonify(RequestController.RequestController().getVendorRequests(id))


@app.route('/requests')
def createRequest():
    return jsonify(RequestController.RequestController().getRequests())


@app.route('/requests', methods=['POST'])
def create1():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(RequestController.RequestController().createRequest(data))


@app.route('/requests/<id>/to_completed', methods=['PUT'])
def completeOrder(id):
    return jsonify(RequestController.RequestController().toCompleted(id))


@app.route('/requests/<id>/to_cancelled', methods=['PUT'])
def cancelOrder(id):
    return jsonify(RequestController.RequestController().toCancelled(id))


#
@app.route('/products/<id>/to_deleted', methods=['PUT'])
def deleteProduct1(id):
    return jsonify(ProductController.ProductController().deleteProduct(id))


# getVendorRequests
if __name__ == "__main__":
    app.run(debug=True)
