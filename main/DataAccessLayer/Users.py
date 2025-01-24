from DataAccessLayer.connection import get_connection


def check_credentials(username, password):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT COUNT(*) FROM Users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False