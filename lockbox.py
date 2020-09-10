'''
project: Lockbox
file: lockbox.py
authors: david rademacher & welton king v
desc: a credentials storage app
'''

import cmd, data
from classes import *

# variables
state = states.START_UP
profile = user()

# handles login and account creation
def start():
    global state, profile
    while profile.is_empty():
        inp = cmd.start()
        if inp == 'c': profile = data.create_account(cmd.get_profile()) # create
        if inp == 'l': profile = data.verify_account(cmd.get_profile()) # login
        if inp == 'q': cmd.quit() + data.quit() # quit
    state = states.MAIN_MENU

# handles main menu
def main_menu():
    global state, profile
    inp = cmd.main_menu(profile)
    if inp == 'r': data.do_something() # retrieve
    if inp == 's': data.do_something() # store new
    if inp == 'u': data.do_something() # update existing
    if inp == 'd': data.do_something() # delete existing
    if inp == 'c': data.do_something() # change user
    if inp == 'q': cmd.quit() + data.quit() # quit

# handles program states
def process():
    global state, profile
    while True:
        if state == states.START_UP: start()
        elif state == states.MAIN_MENU: main_menu()
    return 0

# run process
process()
