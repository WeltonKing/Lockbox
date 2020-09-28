'''
project: Lockbox
file: data.py
authors: david rademacher & welton king v
desc: functions that interact with database
'''

import sys
import sqlite3
from sql import *
from classes import msgs

# store new account information on database
def create_account(conn, profile):
    profiles_tbl(conn)
    if verify_account(conn, profile) is msgs.NAME_MISSING: 
        execute(conn, SQL_INSERT_PROFILES, (profile._name, profile._pass))
        return profile
    else:
        return msgs.NAME_TAKEN

# check if account exists and password is correct
def verify_account(conn, profile):
    profiles_tbl(conn)
    c = conn.cursor()
    c.execute(SQL_RETRIEVE_PROFILES)
    proflist = c.fetchall()
    if len(proflist) == 0: return msgs.NAME_MISSING
    
    for i in range(len(proflist)):
        if proflist[i][0] == profile._name:
            if proflist[i][1] == profile._pass:
                return profile
            else:
                return msgs.PASS_INCORRECT
        else:
            return msgs.NAME_MISSING

# establish connection to, or create, the local database
def connect():
    conn = None
    try: conn = sqlite3.connect('database.db')
    except Error as e: print(e)
    finally: return conn

# placeholder function
def do_something(conn):
    return None

# store a new record of credentials in the database
def store_new(conn, params):
    if not params: return
    credentials_tbl(conn)
    execute(conn, SQL_INSERT_CREDENTIALS, params)

# retrieve credentials
# returns 'None' if the table doesn't exist yet
# TODO: return 'None' if the table exists, but is empty
# 		e.g., credentials existed but were deleted
def retrieve(conn):
    c = conn.cursor()
    try:
        c.execute(SQL_RETRIEVE_CREDENTIALS)
        return c.fetchall()
    except sqlite3.OperationalError as e:
        return None

# grab the column names!        
def column_names(conn):
    c = conn.cursor()
    try:
        c.execute(SQL_RETRIEVE_CREDENTIALS + 'LIMIT 1')
        return [desc[0] for desc in c.description]
    except sqlite3.OperationalError as e:
        return None

# verify the 'Credentials' table exists otherwise create it
def credentials_tbl(conn):
    execute(conn, SQL_CREATE_CREDENTIALS_TBL)

# verify the 'Profiles' table exists otherwise create it
def profiles_tbl(conn):
    execute(conn, SQL_CREATE_PROFILES_TBL)

# execute a sql command on the database
def execute(conn, cmd, params=()):
    c = conn.cursor()
    if params: c.execute(cmd, params)
    else: c.execute(cmd)
    conn.commit()

# terminate program
def quit(conn):
    if conn is not None: conn.close()
    sys.exit()
    return 0
