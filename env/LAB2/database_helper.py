#!/usr/bin/python
import sqlite3
from User import User
from Message import Message

def dict_factory(cursor, row): # return dictionary instead of tuple
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def run_query(query):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory # override function
    cur = conn.cursor()
    cur.execute(query)
    conn.commit() # ?
    # close stuff?
    return cur


def create_tables():
    qry = open('database.schema', 'r').read()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(qry)
    conn.commit()
    c.close()
    conn.close()

def get_user_by_email(email):
    cur = run_query("SELECT * FROM User WHERE User.email = '%s'" % email)
    result = cur.fetchone()
    user = User(result["firstname"], result["familyname"], result["email"],\
                        result["city"], result["country"], result["gender"], result["password"])

    print str(user)

    return user


def delete_token(token):
    cur = run_query("DELETE FROM Session WHERE token = '%s'" % token)
    if cur.rowcount == 1:
        return True
    else:
        return False

def get_userId_by_token(token):
    cur = run_query("SELECT userId FROM Session WHERE token = '%s'" % token)
    result = cur.fetchone()

    return result["userId"]

def insert_message(message, toId, fromId):
    cur = run_query("INSERT INTO Message (msg, toId, fromId)\
                    VALUES ('%s',%s, %s)" % (message, toId, fromId))
    if cur.rowcount == 1:
        return True
    else:
        return False
## Funciones nuevas Isma

def insert_token(token, userId):
    cur = run_query("INSERT INTO Session (token, userId)\
                    VALUES('%s',%s)" % (token,userId))
    if cur.rowcount == 1:
        return True
    else:
        return False

def insert_user(user):
    cur = run_query("INSERT INTO User (id, firstname, familyname, gender, city, \
                    country, email, password) \
                    VALUES('%s','%s','%s','%s','%s','%s','%s')" % (User.firstname, \
                    User.familyname, User.gender, User.city, User.country, \
                    User.email, User.password))
    if cur.rowcount == 1:
        return True
    else:
        return False

def change_user_password(userId, password):
    cur = run_query("UPDATE User SET password = '%s' WHERE id = %s" % (password,userId))

    if cur.rowcount == 1:
        return True
    else:
        return False

# not finished yet!!
def get_messages_by_user(userId):
    cur = run_query("SELECT msg, toId, fromId FROM Message WHERE fromId = %s" % userId)
    msgs = cur.fetchall()
    result = []
    for msg in msgs:
        result.append(Message(msg["fromId"],msg["toId"],msg["msg"]))

    return result

def get_user_by_id(userId):
    cur = run_query("SELECT * FROM User WHERE User.id = %s" % userId)
    result = cur.fetchone()
    user = User(result["firstname"], result["familyname"], result["email"],\
                        result["city"], result["country"], result["gender"], result["password"])

    print str(user)

    return user

def get_token(userId):
    cur = run_query("SELECT * FROM Session WHERE userId = %s" % userId)

    result = cur.fetchone()

    return result["token"]


def create_session(token, userId):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO Session VALUES (?,?)", token, userId)
