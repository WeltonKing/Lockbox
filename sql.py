'''
project: Lockbox
file: constants.py
authors: david rademacher & welton king v
desc: contains sql commands
'''

# sql for inserting a new record into the 'Credentials' table
SQL_INSERT_CREDENTIALS = """
	INSERT INTO Credentials(Account, Username, Password)
	VALUES (?, ?, ?)
	"""

# sql for creating the 'Credentials' table
SQL_CREATE_CREDENTIALS_TBL = """
	CREATE TABLE IF NOT EXISTS Credentials (
		Account text,
		Username text,
		Password text
	);
	"""