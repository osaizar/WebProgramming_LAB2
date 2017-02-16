#!/usr/bin/python

import database_helper as db
import string
import random
from User import User
from Message import Message, MessageList
from ReturnedData import ReturnedData

#app = Flask(__name__)

def token_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def sign_in(email, password):
    userId = db.get_userId_by_email(email)
    if userId == None:
        return ReturnedData(False, "Email not found").createJSON()
    elif db.get_user_by_id(userIds).password != password:
        return ReturnedData(False, "The password is not correct").createJSON()
    else:
        token = token_generator()
        jToken = {}
        jToken["token"] = token
        jToken = json.dumps(jToken)
        if db.insert_token(token, userId):
            return ReturnedData(True, "User signed in", JToken).createJSON()
        else:
            return ReturnedData(False, "Database error").createJSON()



def sign_up(email, password, firstname, familyname, gender, city, country):
    if db.get_userId_by_email(email) != None:  # no success
        return ReturnedData(False, "Email already exists").createJSON()
    else:
        user = User(email, password, firstname,
                    familyname, gender, city, country)
        if db.insert_user(user):
            return ReturnedData(True, "User successfully created").createJSON()
        else:
            return ReturnedData(False, "Database error").createJSON()


def sign_out(token):
    if db.delete_token(token):
        return ReturnedData(True, "Signed out").createJSON()
    else:
        return ReturnedData(False, "Database error").createJSON()


def change_password(token, old_password, new_password):
    userId = db.get_userId_by_token(token)
    if userId == None:
        return ReturnedData(False, "The token is not correct").createJSON()
    elif db.get_user_by_id(userIds).password != old_password:
        return ReturnedData(False, "The password is not correct").createJSON()
    else:
        if db.change_user_password(userId, new_password):
            return ReturnedData(True, "Password changed").createJSON()
        else:
            return ReturnedData(False, "Database error").createJSON()


def get_user_data_by_token(token):
    if userId = db.get_userId_by_token(token) == None:
        return ReturnedData(False, "Invalid Token").createJSON()
    else:
        if userId == None:
            return ReturnedData(False, "Invalid email").createJSON()
        else:
            user = db.get_user_by_id(userId)

            return ReturnedData(True, "User found", user.createJSON())



def get_user_data_by_email(email):
    userId = db.get_userId_by_email(email) == None:

    if userId == None:
        return ReturnedData(False, "Invalid email").createJSON()
    else:
        user = db.get_user_by_id(userId)
        return ReturnedData(True, "User found", user.createJSON())



def get_user_messages_by_token(token):
    userId = db.get_userId_by_token(token)

    if userId == None:
        return ReturnedData(False, "Invalid Token").createJSON()
    else:
        messages = db.get_messages_by_user(userId)
        return ReturnedData(True, "Messages found", messages.createJSON()).createJSON()




def get_user_messages_by_email(token, email):
    if db.get_userId_by_token(token) == None:
        return ReturnedData(False, "Invalid Token").createJSON()
    else:
        userId = db.get_userId_by_email(email)
        if userId == None:
            return ReturnedData(False, "Invalid Token").createJSON()
        else:
            messages = db.get_messages_by_user(userId)
            return ReturnedData(True, "Messages found", messages.createJSON()).createJSON()


def post_message(message, reader, writer):
    msg = Message(writer, reader, message)
    toId = get_userId_by_email(msg.reader)
    if toId == None:
        return ReturnedData(False, "Invalid reader").createJSON()
    fromId = get_userId_by_email(msg.writer)
    else if fromId == None:
        return ReturnedData(False, "Invalid writer").createJSON()
    else
        db.insert_message(msg)
        return ReturnedData(True, "Message sent").createJSON()
