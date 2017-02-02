#!/usr/bin/python

import database_helper
from User import User
from Message import Message
from ReturnedData import ReturnedData

app = Flask(__name__)

def sign_in():


def sign_up(email, password, firstname, familyname, gender, city, country):
    if get_user_by_email(email) != None: # no success
        return ReturnedData(False, "Email already exists", None).createJSON()
    else:
        user = User(email, password, firstname, familyname, gender, city, country)
        if insert_user(user):
            return ReturnedData(True, "User successfully created", None).createJSON()
        else:
            return ReturnedData(False, "Database error", None).createJSON()



def sign_out():


def change_password():

# Empieza Isma

def get_user_data_by_token():


def get_user_data_by_email():


def get_user_messages_by_token():


def get_user_messages_by_email(token,email):
    if get_userId_by_token(token) == None:
        return ReturnedData(False, "Invalid Token", None).createJSON()
    else:
        user = get_user_by_email(email)
        if user == None:
            return ReturnedData(False, "Invalid email", None).createJSON()
        else:
            messages = get_messages_by_user(user.id)
            rData = ReturnedData(True, "Messages found")
            for msg in messages:
                rData.addToData(msg.createJSON())

            return rData.createJSON()


def post_message():
