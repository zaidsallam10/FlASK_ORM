from itsdangerous import Serializer
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products, product_types
# from schemas import UserSchema


class Request(db.Model):
    RequestStatus = request_statuses.RequestStatus
    Product = products.Product
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    request_status_id = db.Column(db.Integer, db.ForeignKey('request_statuses.id'), nullable=False)
    request_status = db.relationship('RequestStatus')
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    customer = db.relationship('User')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship('Product')
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, body):
        self.request_status_id = body.get("request_status_id")
        self.customer_id = body.get("customer_id")
        self.product_id = body.get("product_id")

class UserSchema(marshmallow.ModelSchema):
    id = fields.Int(dump_only=True)
    user_type_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email_address = fields.Str()
    password = fields.Str()
    address = fields.Str()
    age = fields.Str()
    sex = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    social_id = fields.Str()
    mobile_number = fields.Str()
    profile_picture = fields.Str()



class RequestSchema(marshmallow.ModelSchema):
    id = fields.Int(dump_only=True)
    request_status_id = fields.Int()
    request_status = fields.Nested(request_statuses.RequestStatusSchema)
    customer_id = fields.Int()
    customer = fields.Nested(UserSchema)
    product_id = fields.Int()
    product = fields.Nested(products.ProductSchema)
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()



