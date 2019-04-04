from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products, product_types
# from schemas import UserSchema

class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),nullable=False)
    image = db.Column(db.String)
  

    def __init__(self, body):
        self.product_id = body.get("product_id")
        self.image = body.get("image")
        


class ProductImageSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        product_id = fields.Int()
        image = fields.Str()









        