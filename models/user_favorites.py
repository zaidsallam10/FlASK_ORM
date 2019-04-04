from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products,product_types
# from schemas import UserSchema

class UserFavorite(db.Model):
    __tablename__ = 'user_favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_type_id = db.Column(db.Integer)
  

    def __init__(self, body):
        self.user_id = body.get("user_id")
        self.product_type_id = body.get("product_type_id")
        




class UserFavouriteSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        user_id = fields.Int()
        product_type_id = fields.Int()









        