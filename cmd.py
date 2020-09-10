'''
project: Lockbox
file: cmd.py
authors: david rademacher & welton king v
desc: handles cmd line interface
'''

import getpass, sys
from os import system
from constants import *
from classes import *

# login and account creation interface
def start():
	inp = ''
	while inp not in ('c', 'l', 'q'): inp = print_cmds (LOGIN_CMDS, True)
	return inp

# username and pass input interface
def get_profile():
	username = input(' Username: ')
	password = getpass.getpass(' Password: ')
	return user(username, password)

# main menu interface
def main_menu(user):
	print_header()
	print(f' Welcome, {user}!\n')
	inp = print_cmds(MENU_CMDS)
	return inp

# prints a command list given a tuple of strings and returns input
def print_cmds(options, header=False):
	if header: print_header()
	print(' Commands:')
	for option in options:
		print(f'   - [{option[0]}]{option[1:]}')
	inp = input('\n   .: ').lower()
	print()
	return inp

# prints program header
def print_header():
	clear_term()
	print('\n-------------------- Lockbox alpha --------------------\n')

# clears terminal (from stackoverflow)
def clear_term():
	system('cls||clear')

# prints goodbye message
def quit():
	clear_term()
	print('\nGoodbye!\n')
	return 0
