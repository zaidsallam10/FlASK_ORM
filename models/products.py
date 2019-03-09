from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products,product_types
# from schemas import UserSchema

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name_english = db.Column(db.String())
    name_arabic = db.Column(db.String())
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'), nullable=False)
    product_type = db.relationship('ProductType')

    vendor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vendor = db.relationship('User')

    price = db.Column(db.Float())
    description = db.Column(db.Text())
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def __init__(self, body):
        self.name_english = body.get("name_english")
        self.name_arabic = body.get("name_arabic")
        self.product_type_id = body.get("product_type_id")
        self.vendor_id = body.get("vendor_id")
        self.price = body.get("price")
        self.description = body.get("description")



class ProductType(db.Model):
    __tablename__ = 'product_types'
    id = db.Column(db.Integer, primary_key=True)
    type_arabic = db.Column(db.String())
    type_english = db.Column(db.String())
    active = db.Column(db.Boolean)
    image = db.Column(db.String())



class ProductTypeSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        type_arabic = fields.Str()
        type_english = fields.Str()
        active = fields.Str()
        image = fields.Str()

class ProductSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        name_english =fields.Str()
        name_arabic = fields.Str()
        product_type_id = fields.Int()
        product_type = fields.Nested(ProductTypeSchema)
        # vendor = fields.Nested(UserSchema.UserSchema)
        vendor_id = fields.Int()
        price = fields.Int()
        description = fields.Str()
        created_at = fields.Str()
        updated_at = fields.Str()
        deleted_at = fields.Str()






