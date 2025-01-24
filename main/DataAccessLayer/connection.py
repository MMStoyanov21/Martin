import pyodbc
def get_connection():
    try:
        connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};SERVER=Martins-laptop; Database=Users; Trusted_Connection=yes;")
        return connection
    except Exception as error:
        print(error)
