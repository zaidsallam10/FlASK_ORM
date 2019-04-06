from flask import jsonify
import json
from models import requests, products, users,channels,channel_users,channel_msgs
from sqlalchemy import and_
from app import db
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_


class ChatController:
    requests_table = requests.Request
    request_schema = requests.RequestSchema
    products_table = products.Product
    product_schema = products.ProductSchema

    channels_table = channels.Channel
    channel_schema = channels.ChannelSchema
    channel_users_table = channel_users.ChannelUser
    channel_user_schema = channel_users.ChannelUserSchema
    channel_msgs_table = channel_msgs.ChannelMsg
    channel_msg_schema = channel_msgs.ChannelMsgSchema



    def __init__(self):
        print("welcome to ChatController")



    def getAllChannels(self):
        db.session.commit()
        query = self.channels_table.query.all()
        channel_schema = channels.ChannelSchema(many=True)
        return channel_schema.dump(query)


        
    def createChannel(self,body):
        print(body)
        channel = channels.Channel(body)
        db.session.add(channel)
        db.session.commit()
        db.session.refresh(channel)
        users = (body.get("users"))
        for element in users:
            data = {
             "channel_id": channel.id,
             "user_id": element
                    }
            channel_users1 = channel_users.ChannelUser(data)
            db.session.add(channel_users1)
            db.session.commit()
        schema = channels.ChannelSchema(many=False)
        return schema.dump(channel)



    def getVendorChannels(self, vendor_id):
        db.session.commit()
        two = self.channels_table.query.filter(self.channels_table.vendor_id == vendor_id).all()
        schema = channels.ChannelSchema(many=True)
        return schema.dump(two)


    def getCustomerChannels(self, user_id):
        db.session.commit()
        two = self.channel_users_table.query.filter(self.channel_users_table.user_id == user_id).all()
        schema = channel_users.ChannelUserSchema(many=True)
        return schema.dump(two)

    def getChatsByChannelId(self, channel_id):
        db.session.commit()
        two = self.channel_msgs_table.query.filter(self.channel_msgs_table.channel_id == channel_id).all()
        schema = channel_msgs.ChannelMsgSchema(many=True)
        return schema.dump(two)


    def createMsg(self, body):
        data = self.channel_msgs_table(body)
        db.session.add(data)
        db.session.commit()
        return body
