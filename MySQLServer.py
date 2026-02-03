import mysql.connector

connection = None

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='@0725327881Ss'  # Use your password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database safely
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:  # <- Handles MySQL-specific exceptions
    print(f"Error while connecting to MySQL: {err}")

finally:
    # Close the connection
    if connection and connection.is_connected():
        cursor.close()
        connection.close()

