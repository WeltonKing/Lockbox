'''
project: Lockbox
file: cmd_interface.py
author: david rademacher
'''

from os import system

class user:
	def __init__(self, name, password):
		self._name = name
		self._pass = password

	def __repr__(self):
		return '{user: self._name}'
		
	def __str__(self):
		return self._name


def print_main_menu(user=None):
	system('cls||clear') # from stackoverflow - clears the terminal
	print('\n-------------------- Lockbox alpha --------------------\n')
	if user is not None: print(f' Welcome, {user}!')
	print('\n Commands')
	if user is None:
		print('   - [C]reate new account')
		print('   - [L]og in to existing account')
	else:
		print('   - [R]etrieve your list of credentials')
		print('   - [S]tore new credentials')
		print('   - [U]pdate credentials')
		print('   - [D]elete credentials')
		print('   - [C]hange users')
	print('   - [Q]uit')
	return input('\n   .: ')

example = user('etherbyte', 'brazilrocks77')

print(print_main_menu())
print(print_main_menu(example))