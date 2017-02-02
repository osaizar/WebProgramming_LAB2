#!/usr/bin/python

import database_helper as db
from User import User
from Message import Message
from ReturnedData import ReturnedData

#app = Flask(__name__)

def sign_in():
    pass


def sign_up(email, password, firstname, familyname, gender, city, country):
    #if db.get_userId_by_email(email) != None: # no success
    if False:
        return ReturnedData(False, "Email already exists", None).createJSON()
    else:
        user = User(email, password, firstname, familyname, gender, city, country)
        if db.insert_user(user):
            return ReturnedData(True, "User successfully created", None).createJSON()
        else:
            return ReturnedData(False, "Database error", None).createJSON()



def sign_out():
    pass


def change_password():
    pass

# Empieza Isma

def get_user_data_by_token():
    pass


def get_user_data_by_email():
    pass


def get_user_messages_by_token():
    pass


def get_user_messages_by_email(token,email):
    #if db.get_userId_by_token(token) == None:
    if False:
        return ReturnedData(False, "Invalid Token", None).createJSON()
    else:
        userId = db.get_userId_by_email(email)
        #if user == None:
        if False:
            return ReturnedData(False, "Invalid email", None).createJSON()
        else:
            messages = db.get_messages_by_user(userId)
            rData = ReturnedData(True, "Messages found")
            for msg in messages:
                rData.addToData(msg.createJSON())

            return rData.createJSON() # Funciona?


def post_message():
    pass
