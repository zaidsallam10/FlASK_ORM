from itsdangerous import Serializer
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_type_id = db.Column(db.Integer)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email_address = db.Column(db.String())
    password = db.Column(db.String())
    address = db.Column(db.String())
    age = db.Column(db.Integer)
    sex = db.Column(db.Enum('male', 'female', 'other'))
    status = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)
    social_id = db.Column(db.String())

    def __init__(self, body):
        self.user_type_id = body.get("user_type_id")
        self.first_name = body.get("first_name")
        self.last_name = body.get("last_name")
        self.email_address = body.get("email_address")
        self.password = body.get("password")
        self.address = body.get("address")
        self.age = body.get("age")
        self.sex = body.get("sex")
        self.status = body.get("status")
        self.social_id = body.get("social_id")


# serialization process
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