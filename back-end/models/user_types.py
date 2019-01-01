from itsdangerous import Serializer
from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import inspect


class UserType(db.Model):
    __tablename__ = 'user_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return '<id {}>'.format(self.id)
