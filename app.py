from flask import Flask, session, jsonify, abort, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:300/shopping_system_v1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:LEOmessi123#@18.219.85.157:3306/shopping_system_v1'
app.config['SQLALCHEMY_ECHO'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
# mysql = MySQL(app)
db = SQLAlchemy(app)

marshmallow = Marshmallow(app)
from controller import UserController
from controller import ProductController
from controller import RequestController

# CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/users', methods=['GET'])
def allUsers():
    return jsonify(UserController.UserController().getAllUsers()[0])


@app.route('/vendors', methods=['GET'])
def allVendors():
    return jsonify(UserController.UserController().getAllVendors()[0])


@app.route('/users/<id>')
def userById(id):
    return jsonify(UserController.UserController().getById(id=id)[0])


@app.route('/signup', methods=['POST'])
def signUp():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().signUp(data))


@app.route('/login', methods=['POST'])
def loginUser():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().login(data['email_address'], data['password'])[0])

@app.route('/loginFacebook', methods=['POST'])
def loginFacebook():
    if not request.form and not request.get_json():
        abort(400)
    data = request.get_json() or request.form
    return jsonify(UserController.UserController().loginFacebook(data['social_id'])[0])

# 

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
    return jsonify(ProductController.ProductController().getAll()[0])


@app.route('/products/<id>')
def getProductById(id):
    return jsonify(ProductController.ProductController().getById(id=id)[0])


@app.route('/products/types')
def getProductTypes():
    return jsonify(ProductController.ProductController().getAllTypes()[0])


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
    return jsonify(UserController.UserController().holdedAccounts()[0])


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
    return jsonify(UserController.UserController().getMyProducts(id)[0])


# getCustomerRequests
@app.route('/users/<id>/requests', methods=['GET'])
def getCustomerRequests(id):
    return jsonify(RequestController.RequestController().getCustomerRequests(id)[0])


@app.route('/users/<id>/closed_requests', methods=['GET'])
def getCustomerClosedRequests(id):
    return jsonify(RequestController.RequestController().getCustomerClosedRequests(id)[0])


# getCustomerClosedRequests


# getVendorRequests
@app.route('/users/<id>/orders', methods=['GET'])
def getVendorRequests(id):
    return jsonify(RequestController.RequestController().getVendorRequests(id)[0])


@app.route('/requests')
def createRequest():
    return jsonify(RequestController.RequestController().getRequests()[0])


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
