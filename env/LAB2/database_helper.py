#!/usr/bin/python
import sqlite3
from classes import User

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



def create_session(token, userId):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO Session VALUES (?,?)", token, userId)


get_user_by_email("mail.com") # debug
