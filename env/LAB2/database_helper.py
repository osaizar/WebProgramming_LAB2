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
    conn.commit()
    return cur


def create_tables():
    qry = open('database.schema', 'r').read()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(qry)
    conn.commit()
    c.close()
    conn.close()

# Public functions

def get_userId_by_email(email): #TODO: check get
    cur = run_query("SELECT id FROM User WHERE User.email = '%s'" % email)

    result = cur.fetchone()
    userId = result["id"]

    return userId


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

def insert_message(message): #TODO: Check users
    toId = get_userId_by_email(message.reader)
    fromId = get_userId_by_email(message.writer)

    print "[Message] To: "+str(toId)+" From:"+str(fromId) # debug

    cur = run_query("INSERT INTO Message (msg, toId, fromId)\
                    VALUES ('%s',%s, %s)" % (message.content, toId, fromId))
    if cur.rowcount == 1:
        return True
    else:
        return False


def insert_token(token, userId):
    cur = run_query("INSERT INTO Session (token, userId)\
                    VALUES('%s',%s)" % (token,userId))
    if cur.rowcount == 1:
        return True
    else:
        return False

def insert_user(user):
    cur = run_query("INSERT INTO User (firstname, familyname, gender, city, \
                    country, email, password) \
                    VALUES('%s','%s','%s','%s','%s','%s','%s')" % (user.firstname, \
                    user.familyname, user.gender, user.city, user.country, \
                    user.email, user.password))
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

def get_messages_by_user(userId):
    cur = run_query("SELECT msg, toId, fromId FROM Message WHERE toId = %s" % userId)

    msgs = cur.fetchall()
    result = []
    for msg in msgs:
        writer = get_user_by_id(msg["fromId"])
        reader = get_user_by_id(userId)
        result.append(Message(writer.email,reader.email,msg["msg"]))

    return result

def get_user_by_id(userId):
    cur = run_query("SELECT * FROM User WHERE User.id = %s" % userId)

    result = cur.fetchone()
    user = User(result["email"], result["password"], result["firstname"],\
                        result["familyname"], result["gender"], result["city"], result["country"])

    return user

def get_token(userId):
    cur = run_query("SELECT * FROM Session WHERE userId = %s" % userId)

    result = cur.fetchone()

    return result["token"]
