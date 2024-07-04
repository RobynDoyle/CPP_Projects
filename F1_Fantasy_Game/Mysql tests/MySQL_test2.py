import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            # Create a cursor object
            cursor = connection.cursor()

            
            # Execute a query
            cursor.execute("SELECT Points FROM 2023_season_race_data WHERE `Race number` = 9 AND `First name` = 'Max'; ")

            # Fetch the results
            rows = cursor.fetchall()

            # Print the results
            for row in rows:
                print(row)

            # Close the cursor
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            # Close the connection
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_mysql()
