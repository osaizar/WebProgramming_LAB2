#!/usr/bin/python
import sqlite3


def create_tables():
    qry = open('database.schema', 'r').read()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(qry)
    conn.commit()
    c.close()
    conn.close()


def get_user_by_email(email):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM User WHERE User.email = '"+email+"'")
    rows = c.fetchall()

    for row in rows:
        print row



def create_session(token, userId):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO Session VALUES (?,?)", token, userId)


get_user_by_email("mail.com")
