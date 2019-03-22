from flask import jsonify
import json
from models import users
from sqlalchemy import and_
from app import db
from sqlalchemy.orm import Session
from models import products


class UserController:
    users_table = users.User
    users_schema = users.UserSchema
    products_model = products.Product
    products_types_model = products.ProductType

    def __init__(self):
        print("serController")

    def getAllUsers(self):
        db.session.commit()
        data = self.users_table.query.filter(self.users_table.user_type_id == 1).all()
        my_schema = self.users_schema(many=True)
        return my_schema.dump(data)

    def getAllVendors(self):
        db.session.commit()
        query = self.users_table.query.filter(self.users_table.user_type_id == 2)
        schema = self.users_schema(many=True)
        return schema.dump(query)

    def getById(self, id):
        db.session.commit()
        query = self.users_table.query.filter(self.users_table.id == id).first()
        my_schema = self.users_schema(many=False)
        return my_schema.dump(query)

    def login(self, email_address, password):
        query = self.users_table.query.filter(
            and_(
                self.users_table.email_address == email_address, self.users_table.password == password)).first()
        my_schema = self.users_schema(many=False)
        return my_schema.dump(query)

    def loginFacebook(self, social_id):
        query = self.users_table.query.filter(
            and_(
                self.users_table.social_id == social_id)).first()
        my_schema = self.users_schema(many=False)
        return my_schema.dump(query)    


    def loginVendor(self, email_address, password):
        query = self.users_table.query.filter(
            and_(
                self.users_table.email_address == email_address, self.users_table.password == password,
                self.users_table.user_type_id == 2)).first()
        my_schema = self.users_schema(many=False)
        return my_schema.dump(query)

    def loginAdmin(self, email_address, password):
        query = self.users_table.query.filter(
            and_(
                self.users_table.email_address == email_address, self.users_table.password == password,
                self.users_table.user_type_id == 3)).first()
        my_schema = self.users_schema(many=False)
        return my_schema.dump(query)

    def signUp(self, body):
        session = Session(db)
        address = self.users_table(body)
        db.session.add(address)
        db.session.commit()
        return body

    def holdAccount(self, id):
        account = self.users_table.query.filter_by(id=id).first()
        account.status = 0
        db.session.commit()
        user_schema = users.UserSchema(many=False)
        return user_schema.dump(account)

    def unHoldAccount(self, id):
        account = self.users_table.query.filter_by(id=id).first()
        account.status = 1
        db.session.commit()
        user_schema = users.UserSchema(many=False)
        return user_schema.dump(account)

    def holdedAccounts(self):
        query = self.users_table.query.filter(self.users_table.status == 0).all()
        user_schema = users.UserSchema(many=True)
        return user_schema.dump(query)

    # this function to get my products as a vendor
    def getMyProducts(self, id):
        db.session.commit()
        query = self.products_model.query.filter(self.products_model.vendor_id == id).all()
        product_schema = products.ProductSchema(many=True)
        return product_schema.dump(query)
