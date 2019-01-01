from flask import jsonify
import json
from models import requests, products, users
from sqlalchemy import and_
from app import db
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_


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
            and_(self.requests_table.customer_id == id,
                 or_(self.requests_table.request_status_id == 3, self.requests_table.request_status_id == 4))).all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def getVendorRequests(self, id):
        query = self.requests_table.query.join(products.Product).filter_by(vendor_id=id).all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def getRequests(self):
        query = self.requests_table.query.all()
        request_schema = requests.RequestSchema(many=True)
        return request_schema.dump(query)

    def createRequest(self, body):
        data = self.requests_table(body)
        db.session.add(data)
        db.session.commit()
        return body

    def toCompleted(self, id):
        data = self.requests_table.query.filter_by(id=id).first()
        data.request_status_id = 3
        db.session.commit()
        request_schema = requests.RequestSchema(many=False)
        return request_schema.dump(data)

    def toCancelled(self, id):
        data = self.requests_table.query.filter_by(id=id).first()
        data.request_status_id = 4
        db.session.commit()
        request_schema = requests.RequestSchema(many=False)
        return request_schema.dump(data)


