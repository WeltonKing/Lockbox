'''
project: Lockbox
file: sql.py
authors: david rademacher & welton king v
desc: contains sql commands
'''

# sql for inserting a new record into the 'Credentials' table
SQL_INSERT_CREDENTIALS = """
	INSERT INTO Credentials(Account, Username, Password, "Last Updated")
	VALUES (?, ?, ?, ?)
	"""

# sql for retrieving the user's list of stored credentials
# straightforward
SQL_RETRIEVE_CREDENTIALS = """
	SELECT * FROM Credentials
	"""

# sql for creating the 'Credentials' table
SQL_CREATE_CREDENTIALS_TBL = """
	CREATE TABLE IF NOT EXISTS Credentials (
		Account text,
		Username text,
		Password text,
		"Last Updated" text
	);
	"""
