import pyodbc
def get_connection():
    try:
        print("Connected")
        connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-GS9UCIK; Database=CustomerDB;Trusted_Connection=yes;")
    except Exception as error:
        print(error)
    finally:
        print("Connected successfully")
        return connection
connection = get_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM Customers")
data = cursor.fetchall()
for row in data:
    print(row)