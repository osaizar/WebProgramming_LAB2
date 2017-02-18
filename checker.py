#!/usr/bin/python

from flask import Flask, request, render_template, abort
import database_helper as db
import string
import random
import json
import re

from User import User
from Message import Message, MessageList
from ReturnedData import ReturnedData

MAIL_RE = "[^@]+@[^@]" # something followed by @ followed by something

def check_sign_in_data(data):
    if data == None:
        abort(400)
    try:
        if not (data["email"] and data["password"]):
            return False, ReturnedData(False, "Fill all fields").createJSON()
    except:
        abort(400)
    # Check spaces?
    return True, None


def check_sign_up_data(data):
    if data == None:
        abort(400)
    try:
        if not (data["email"] and data["firstname"] and data["familyname"] \
            and data["gender"] and data["password"] and data["city"] and data["country"]):

            return False, ReturnedData(False, "Fill all fields").createJSON()
    except:
        abort(400)

    if data["email"].isspace() or data["firstname"].isspace() or data["familyname"].isspace() \
        or data["gender"].isspace() or data["password"].isspace() or data["city"].isspace() \
        or data["country"].isspace():

        return False, ReturnedData(False, "You can't fill the fields with spaces").createJSON()
    elif len(data["password"]) < 6:
        return False, ReturnedData(False, "The password is too short").createJSON()
    elif not re.match(MAIL_RE, data["email"]):
        return False, ReturnedData(False, "The email is not valid").createJSON()
    elif data["gender"] != "Male" and data["gender"] != "Female":
        return False, ReturnedData(False, "The gender is not valid").createJSON()
    else:
        return True, None

def check_change_password_data(data):
    if data == None:
        abort(400)
    elif data["token"] == None or data["old_password"] == None or data["new_password"] == None:
        abort(400)
    elif len(data["new_password"]) < 6:
        return False, ReturnedData(False, "The password is too short").createJSON()
    else:
        return True, None

def check_token(data):
    if data == None:
        abort(400)
    elif data["token"] == None:
        abort(400)
    else:
        return True, None

def check_token_and_email(data):
    if data == None:
        abort(400)
    elif data["token"] == None or data["email"] == None:
        abort(400)
    else:
        return True, None

def check_send_message_data(data):
    if data == None:
        abort(400)
    elif data["token"] == None or data["msg"] == None or data["reader"] == None:
        abort(400)
    elif (not data["msg"]) or data["msg"].isspace():
        return False, ReturnedData(False, "The message is too short").createJSON()
    else:
        return True, None
