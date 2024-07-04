import mysql.connector
from mysql.connector import Error

def Welcome():
    print("*************************************************************************")
    playername = input("Enter player name: ")
    print("Your player name is: " + playername)


def query_with_variables(Race, Driver, Driver_two):
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

            # Use parameterized query
            query = "SELECT Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Race, Driver, Race, Driver_two))

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

    return rows


def Select_driver():
    if __name__ == "__main__":
        # Set variables
        Race = 1
        Driver = input("Enter Driver 1's initials eg. VER: ")
        Driver_two = input("Enter Driver 2's initials eg. VER: ")
        
        results = query_with_variables(Race, Driver, Driver_two)
        score = results
        print("Your score for this weeks race: ")
        print(score)

def main():
    Welcome()

    Select_driver()
    

main()


