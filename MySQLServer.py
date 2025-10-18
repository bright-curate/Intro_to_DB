import mysql.connector

def create_database():
    """Create the alx_book_store database if it does not already exist."""
    try:
        # Establish connection to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',             # replace with your username
            password='Bright@6124'   # replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle connection or execution errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

