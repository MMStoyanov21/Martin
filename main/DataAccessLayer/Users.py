from DataAccessLayer.connection import get_connection, get_connectionTeacher

def check_credentials_students(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if username exists
        query = "SELECT password FROM Students WHERE userName = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        # If username doesn't exist
        if not result:
            return False

        # Check if the provided password matches
        stored_password = result[0]
        return password == stored_password

    except Exception as e:
        print(f"Error: {e}")
        return False
def check_credentials_teacher(username, password):
    try:
        conn = get_connectionTeacher()
        cursor = conn.cursor()
        query = "SELECT teacherPassword FROM Teachers WHERE TeacherUsername = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if not result:
            return False
        stored_password = result[0]
        return password == stored_password
    except Exception as e:
        print(f"Error: {e}")
        return False


