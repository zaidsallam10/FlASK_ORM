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


@app.route('/')
def allUsers():
    return ("hhhhh")




# getVendorRequests
if __name__ == "__main__":
    app.run()
