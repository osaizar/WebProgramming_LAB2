#!/usr/bin/python

from User import User
from Message import Message
from ReturnedData import ReturnedData
import database_helper as db
import server
import os


def test_server():
    response = server.sign_up("oier@mail.com1", "pw", "Oier", "Saizar", "M", "Tolosa", "EH")
    server.sign_up("otherUser@mail.com", "pwOU", "OTHER", "OTHERFAMILY", "M", "Sevilla", "EH")
    print response
    response = server.sign_in("oier@mail.com1", "pw")
    print response


    message1 = Message("oier@mail.com1", "oier@mail.com1", "message1")
    message2 = Message("oier@mail.com1", "oier@mail.com1", "message2")
    message3 = Message("oier@mail.com1", "oier@mail.com1", "message3")

    db.insert_message(message1)
    db.insert_message(message2)
    db.insert_message(message3)

    response = server.get_user_messages_by_email("thisisarandomtoken","oier@mail.com1")
    print response

    response = server.get_user_data_by_email("thisisarandomtoken","otherUser@mail.com")

test_server()
