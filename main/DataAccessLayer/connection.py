import pyodbc
def get_connection():
    try:
        connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};SERVER=Martins-laptop; Database=Users; Trusted_Connection=yes;")
        return connection
    except Exception as error:
        print(error)
def get_connectionTeacher():
    try:
        connections = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};SERVER=Martins-laptop; Database=Teacher; Trusted_Connection=yes;")
        return connections
    except Exception as error:
        print(error)