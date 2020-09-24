'''
project: Lockbox
file: cmd.py
authors: david rademacher & welton king v
desc: handles cmd line interface
'''

import getpass, sys
from os import system
from menus import *
from classes import *

# login and account creation interface
def start():
	inp = ''
	while inp not in ('c', 'l', 'q'): inp = print_cmds (MENU_LOGIN, True)
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
	return (account, username, password)

# prints a command list given a tuple of strings and returns input
def print_cmds(options, header=False):
	if header: print_header()
	print(' Commands:')
	for option in options:
		print(f'   - [{option[0]}]{option[1:]}')
	inp = input('\n   .: ').lower()
	print()
	return inp

# prints a prompt for filling out data fields
def print_prompt(prompt, header=False):
	if header:
		print_header()
		print(' Fill out the following fields')
		print(' (or return \'c\' anytime to cancel)\n')
	inp = input(f' {prompt}: ')
	return inp

# checks to see if the input matches the force cancel character (c)
def check_cancel(inp):
	if inp.lower() == 'c': return True
	return False

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
