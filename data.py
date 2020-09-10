'''
project: Lockbox
file: cmd_interface.py
authors: david rademacher & welton king v
desc: functions that interact with database
'''

import sys

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

# placeholder function
def do_something():
    return None

# terminate program
def quit():
    sys.exit()
    return 0
