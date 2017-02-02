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


def get_user_data_by_token():


def get_user_data_by_email():


def get_user_messages_by_token():


def get_user_messages_by_email():


def post_message():
