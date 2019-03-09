from app import db, marshmallow
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from marshmallow import fields


# class UserSchema(marshmallow.ModelSchema):
#     id = fields.Int(dump_only=True)
#     user_type_id = fields.Int()
#     first_name = fields.Str()
#     last_name = fields.Str()
#     email_address = fields.Str()
#     password = fields.Str()
#     address = fields.Str()
#     age = fields.Str()
#     sex = fields.Str()
#     created_at = fields.Str()
#     updated_at = fields.Str()
#     deleted_at = fields.Str()
#     status = fields.Int()
