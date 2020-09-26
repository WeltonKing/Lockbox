'''
project: Lockbox
file: cmd_interface.py
authors: david rademacher & welton king v
desc: functions that interact with database
'''

import sys
import sqlite3
from sql import *

# store new account information on database
def create_account(profile):
    verification = True
    if verification is False: return None
    else: return profile

# check if account exists and password is correct
def verify_account(profile):
    verification = True
    if verification is False: return None
    else: return profile

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
# some duplication of what's going on in the execute() method,
# but this seems to need a cursor to use .fetchall().
# didn't want to do too much refactoring here!
def retrieve(conn):
    c = conn.cursor()
    c.execute(SQL_RETRIEVE_CREDENTIALS)
    return c.fetchall()

# verify the 'Credentials' table exists otherwise create it
def credentials_tbl(conn):
    execute(conn, SQL_CREATE_CREDENTIALS_TBL)

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
