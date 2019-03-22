from flask import jsonify
import json
from models import products
# from models import product_types
import jsonpickle
from app import db
# sqlalchemy.orm.lazyload
from sqlalchemy.orm import lazyload, joinedload
import datetime
from sqlalchemy.orm import Session


class ProductController:
    products_model = products.Product
    products_types_model = products.ProductType


    def __init__(self):
        print("ProductController")

    def getAll(self):
        db.session.commit()
        two = self.products_model.query.all()
        product_schema = products.ProductSchema(many=True)
        output = product_schema.dump(two)
        return output


    def getById(self, id):
        db.session.commit()
        two = self.products_model.query.filter(self.products_model.id == id).first()
        product_schema = products.ProductSchema(many=False)
        output = product_schema.dump(two)
        return output

    def getAllTypes(self):
        db.session.commit()
        table = self.products_types_model.query.all()
        product_schema = products.ProductTypeSchema(many=True)
        return product_schema.dump(table)

    def deleteProduct(self, id):
        query = self.products_model.query.filter_by(id=id).first()
        query.deleted_at = datetime.datetime.now()
        db.session.commit()
        product_schema = products.ProductTypeSchema(many=False)
        return product_schema.dump(query)

    def addProduct(self, body):
        product = products.Product(body)
        db.session.add(product)
        db.session.commit()
        return body

    def updateProduct(self, id, body):
        query = self.products_model.query.filter_by(id=id).first()
        schema = products.ProductSchema(many=False)
        schema1 = schema.dump(body)
        query = schema1
        db.session.commit()
        product_schema = products.ProductSchema(many=False)
        return product_schema.dump(query)

    def deleteProduct(self, id):
        data = self.products_model.query.filter_by(id=id).first()
        data.active = 0
        data.deleted_at = datetime.datetime.now()
        db.session.commit()
        request_schema = products.ProductSchema(many=False)
        return request_schema.dump(data)
