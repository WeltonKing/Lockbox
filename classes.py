'''
project: Lockbox
file: classes.py
authors: david rademacher & welton king v
desc: contains class definitions
'''

from enum import Enum

# states of the program
class states(Enum):
    START_UP = 0
    MAIN_MENU = 1
    DISPLAY = 2

# account messages
class msgs(Enum):
    PASS_INCORRECT = 0
    NAME_MISSING = 1
    NAME_TAKEN = 2

# user account object
class user:
    def __init__(self, name='', password=''):
        self._name = name
        self._pass = password

    def is_empty(self):
        return self._name == '' and self._pass == ''

    def __repr__(self):
        return '{user: self._name}'

    def __str__(self):
        return self._name
