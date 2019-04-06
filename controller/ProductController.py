from flask import jsonify
import json
from models import products,product_images,requests
# from models import product_types
import jsonpickle
from app import db
# sqlalchemy.orm.lazyload
from sqlalchemy.orm import lazyload, joinedload
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.orm import load_only


class ProductController:
    products_model = products.Product
    products_types_model = products.ProductType
    product_images_model = product_images.ProductImage
    product_images_schema = product_images.ProductImageSchema
    requests_table = requests.Request
    request_schema = requests.RequestSchema


    def __init__(self):
        print("ProductController")

    def getAll(self):
        db.session.commit()
        two = self.products_model.query.filter(self.products_model.deleted_at == None).all()
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
        print(body)
        product = products.Product(body)
        db.session.add(product)
        db.session.commit()
        db.session.refresh(product)
        images = (body.get("images"))
        for element in images:
            message = {
             "product_id": product.id,
             "image": element
                    }
            product_images1 = product_images.ProductImage(message)
            db.session.add(product_images1)
            db.session.commit()
        product_schema = products.ProductSchema(many=False)
        return product_schema.dump(product)

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



    def getAllMultiRequestsOnProduct(self):
        db.session.commit()
        result = db.engine.execute("select product_id from requests group by requests.product_id having count(requests.id)>1")
        request_schema = requests.RequestSchema(many=True)
        return  request_schema.dump(result)