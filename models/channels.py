from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products, product_types
# from schemas import UserSchema

class Channel(db.Model):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer,nullable=False)
    vendor_id = db.Column(db.Integer)
  

    def __init__(self, body):
        self.product_id = body.get("product_id")
        self.vendor_id = body.get("vendor_id")
        


class ChannelSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        product_id = fields.Int()
        vendor_id = fields.Int()









        