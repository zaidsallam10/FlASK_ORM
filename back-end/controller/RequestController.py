from flask import jsonify
import json
from models import requests, products, users
from sqlalchemy import and_
from app import db
from sqlalchemy.orm import Session


class RequestController:
    requests_table = requests.Request
    request_schema = requests.RequestSchema

    products_table = products.Product
    product_schema = products.ProductSchema

    def __init__(self):
        print("welcome to RequestController")

    def getCustomerRequests(self, id):
        query = self.requests_table.query.filter_by(customer_id=id, request_status_id=1).all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def getCustomerClosedRequests(self, id):
        query = self.requests_table.query.filter(
            (customer_id == id) | (request_status_id == 3) | (request_status_id == 4)).all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def getVendorRequests(self, id):
        query = self.requests_table.query.join(products.Product).filter_by(vendor_id=id).all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def create(self, body):
        print(body)
        session = Session(db)
        # schema = requests.RequestSchema(many=False)
        # schema1 = schema.dump(body)
        data = requests.Request(body)
        # print(data)
        # db.session.add(data)
        # db.session.commit()
        # return body

    def getRequests(self):
        query = self.requests_table.query.all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def createRequest(self, body):
        data = self.requests_table(body)
        db.session.add(data)
        db.session.commit()
        return body
