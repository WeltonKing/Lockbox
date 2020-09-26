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
conn = data.connect()

# handles login and account creation
def start():
    global state, profile, conn
    while profile.is_empty():
        inp = cmd.start()
        if inp == 'c': profile = data.create_account(cmd.get_profile()) # create
        if inp == 'l': profile = data.verify_account(cmd.get_profile()) # login
        if inp == 'q': cmd.quit() + data.quit(conn) # quit
    state = states.MAIN_MENU

# handles main menu
def main_menu():
    global state, profile, conn
    inp = cmd.main_menu(profile)
    # retrieve
    if inp == 'r':
        state = states.DISPLAY
        cmd.print_header(f'{profile}\'s credentials') 
        cmd.print_credentials(data.retrieve(conn), data.column_names(conn)))

    if inp == 's': data.store_new(conn, cmd.store_new()) # store new
    if inp == 'u': data.do_something(conn) # update existing
    if inp == 'd': data.do_something(conn) # delete existing
    if inp == 'c': data.do_something(conn) # change user
    if inp == 'q': cmd.quit() + data.quit(conn) # quit

def display():
    global state
    # pretty bad workaround / not sure of pythonic way to do this
    input('\n\n  Press Enter to go back.')
    state = states.MAIN_MENU

# handles program states
def process():
    global state, profile, conn
    if conn is None:
        data.quit(conn)
    else:
        while True:
            if state == states.START_UP: start()
            elif state == states.MAIN_MENU: main_menu()
            elif state == states.DISPLAY: display()
    return 0

# run process
process()
