'''
project: Lockbox
file: cmd.py
authors: david rademacher & welton king v
desc: handles cmd line interface
'''

import getpass, sys
import os 
from math import floor
from menus import *
from classes import *
from datetime import datetime as dt

# login and account creation interface
def start():
    inp = ''
    print_header()
    while inp not in ('c', 'l', 'q'): inp = print_cmds(MENU_LOGIN)
    return inp

# username and pass input interface
def get_profile():
    username = input(' Username: ')
    password = getpass.getpass(' Password: ')
    return user(username, password)
    
def login_response(profile):
    if type(profile) is user: return True
    if profile == msgs.PASS_INCORRECT: print('\n Incorrect password.')
    if profile == msgs.NAME_MISSING: print('\n Username does not exist.')
    if profile == msgs.NAME_TAKEN: print('\n Username is already taken.')
    enter_to_return()
    return False

# main menu interface
def main_menu(user):
    print_header()
    print(f' Welcome, {user}!\n')
    inp = print_cmds(MENU_MAIN)
    return inp

# interface for handling the record of a new credential
def store_new():
    account = print_prompt('Account', True)
    if check_cancel(account): return ()
    username = print_prompt('Username')
    if check_cancel(username): return ()
    password = print_prompt('Password')
    if check_cancel(password): return ()
    return (account, username, password, dt.now().strftime('%m/%d/%y'))

# printing format for table of credentials
def print_credentials(profile, tbl, cols):
    print_header()
    print(f' {profile}\'s Credentials\n')
    if tbl is None: print(' No credentials to display.')
    else:
        cws = column_widths(tbl, cols)
        print('\n ', end='')
        for i in range(len(cols)): print(f'|{cols[i]: <{cws[i]}}', end='')
        print('\n ', end='')
        for i in range(len(cols)): print('+' + '-' * cws[i], end='')

        print()
        for row in tbl:
            print(' ', end='')
            for i in range(len(row)): print(f'|{row[i]: <{cws[i]}}', end='')
            print()

# calculate column widths given table and column headers
def column_widths(tbl, cols):
    widths = [0] * len(cols)
    padding = 3
    for i in range(len(cols)): widths[i] = len(cols[i]) + padding
    for row in tbl:
        for i in range(len(row)): widths[i] = max(len(row[i]) + padding, widths[i])
    return widths

# prints a command list given a tuple of strings and returns input
def print_cmds(options):
    print(' Commands:')
    for option in options:
        print(f'   - [{option[0]}]{option[1:]}')
    inp = input('\n   .: ').lower()
    print()
    return inp

# prints a prompt for filling out data fields
def print_prompt(prompt, title=False):
    if title is True:
        print_header()
        print(' Fill out the following fields')
        print(' (or return \'c\' anytime to cancel)\n')
    inp = input(f' {prompt}: ')
    return inp

# checks to see if the input matches the force cancel character (c)
def check_cancel(inp):
    if inp.lower() == 'c': return True
    return False

# prints page header
def print_header(title='Lockbox Alpha'):
    clear_term()
    t_width = len(title)
    width = os.get_terminal_size().columns
    hyphens = (floor(width/2) - floor(t_width/2) - 1) 
    print('\n' + '-'*(hyphens-1) + f' {title} ' + '-'*hyphens + '\n')

# stall until user presses 'enter'
def enter_to_return():
    input('\n\n Press \'Enter\' to go back.')

# clears terminal (from stackoverflow)
def clear_term():
    os.system('cls||clear')

# prints goodbye message
def quit():
    clear_term()
    print('\nGoodbye!\n')
    return 0
