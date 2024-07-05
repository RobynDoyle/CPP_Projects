import mysql.connector
from mysql.connector import Error

def Welcome():
    print("**************************************** PLAYER DETAILS ********************************************************\n")
    print("Enter your name and get ready to play!")
    
    playername = input("Enter player name: ")
    print("Your player name is: " + playername + "\n")

    races = input("Choose how many races your wish to play: ")
    print("\nTIP: For a more challenging game, ignore VER and use only other drivers.\n")


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
        # Race needs to iterate ++1 - maybe need to pass it, or iterate when we leave this function
        Race = 1
        print("********************************************** RACE " + str(Race) + " **********************************************************\n")

        print("Driver options are VER PER ALO SAI HAM STR RUS BOT GAS ALB TSU SAR MAG DEV HUL ZHO NOR OCO LEC PIA\n")
        
        

        # No duplicate can be allowed. an if loop needed here, also check for correct formatting.
        Driver = "SAME"
        Driver_two = "SAME"

        while(Driver == Driver_two):
            print("Please select a different driver for each position. Use the drivers initials exactly as shown above")
            while(len(Driver) != 3) or (Driver == Driver_two):
                Driver = input("1st: ")
            while(len(Driver_two) != 3) or (Driver == Driver_two):
                Driver_two = input("2nd: ")

        Driver = Driver.upper()
        Driver_two = Driver_two.upper()

        print("\nYour selection is:\n1st: " + Driver + "\n2nd: " + Driver_two + "\n") 

        Choice = 'X'
        while (Choice != "N" and Choice != 'Y' and Choice != 'n' and Choice != 'y'):
            Choice = input("Enter Y to continue or N to change your selection: ")
        
        if Choice == 'Y':
            print(" ")
        else: Select_driver()
        
        if Choice == 'Y':
            print(" ")
        else: return

        results = query_with_variables(Race, Driver, Driver_two)
        

    
            

        print("Your score for this weeks race: ")
        print(results)

def main():
    Welcome()

    # run select driver for all races = 22 this time. Update overall score var
    Select_driver()
    

main()


