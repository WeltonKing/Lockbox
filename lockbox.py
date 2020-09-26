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
    if inp == 'r': retrieve()
    if inp == 's': store_new()
    if inp == 'u': update_existing()
    if inp == 'd': delete_existing()
    if inp == 'c': change_user()
    if inp == 'q': quit()

# handles the credentials display page
def display():
    global state
    cmd.enter_to_return()
    state = states.MAIN_MENU

# retrieve list of credentials and display on page
def retrieve():
    global state, profile, conn
    cmd.print_credentials(profile, data.retrieve(conn), data.column_names(conn))
    state = states.DISPLAY

# prompt user for new credentials to store
def store_new():
    global state, conn
    data.store_new(conn, cmd.store_new())

# prompt user to update existing credentials
def update_existing():
    global state, conn
    data.do_something(conn)

# prompt user to delete existing credentials
def delete_existing():
    global state, conn
    data.do_something(conn)

# log out
def change_user():
    global state, conn
    data.do_something(conn)

# end program
def quit():
    global state, conn
    cmd.quit() + data.quit(conn)

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
