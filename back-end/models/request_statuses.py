from itsdangerous import Serializer
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect
from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from models import product_types
from sqlalchemy.orm import relationship
from marshmallow import fields


class RequestStatus(db.Model):
    __tablename__ = 'request_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())

    def __init__(self, status):
        self.status = status


class RequestStatusSchema(marshmallow.ModelSchema):
    id = fields.Int(dump_only=True)
    status = fields.Str()
