from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields
from models import request_statuses, users, products, product_types
# from schemas import UserSchema

class ChannelUser(db.Model):
    __tablename__ = 'channel_users'

    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
  

    def __init__(self, body):
        self.channel_id = body.get("channel_id")
        self.user_id = body.get("user_id")
        


class ChannelUserSchema(marshmallow.ModelSchema):
        id = fields.Int(dump_only=True)
        channel_id = fields.Int()
        user_id = fields.Int()









        