import mysql.connector
from mysql.connector import Error

def Get_player_name():
    print("**************************************** PLAYER DETAILS ********************************************************\n")
    print("Enter your name and get ready to play!")
    
    playername = input("Enter player name: ")
    print("Your player name is: " + playername + "\n")

    return playername 

def Choose_how_many_races():

    # Choose how many races will be played
    races = 0
    while races < 1 or races > 22: 
        races = int(input("2023 had 22 races. How many do you wish to play? Input whole number: "))


    races_int = int(races)
    races_amount = []
    for i in range(1, races_int + 1):
        races_amount.append(i)

    # print(races_amount)

    race_names = ["bahrain", "saudi-arabia", "australia", "azerbaijan", "miami", "monaco", "spain", "canada", "austria", "great-britain", "hungary", "belgium", "netherlands", "italy", "singapore", "japan", "qatar", "united-states", "mexico", "brazil", "las-vegas", "abu-dhabi"]
    # Using list comprehension to convert each item to uppercase
    races_uppercase_list = [item.upper() for item in race_names]
    
    # Create list for races in this session
    Races_this_session = []
    # print races selected
    print("The races you will compete in are: ")
    for i in range(0,races):
        print(races_uppercase_list[i])
        Races_this_session.append(races_uppercase_list[i])


    # print(races_uppercase_list)
    print("\nTIP: For a more challenging game, ignore VER and use only other drivers.\n")
    return Races_this_session

def query_with_variables(Count, Driver, Driver_two):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )

        if connection.is_connected():
            # print("Successfully connected to the database")
            # Create a cursor object
            cursor = connection.cursor()

            # Use parameterized query
            query = "SELECT Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Count, Driver, Count, Driver_two))

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
            # print("MySQL connection is closed")
    
    points_counter = 0
    for tup in rows:
        points_counter += sum(tup)
    

    return points_counter

def query_for_driver_list():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )

        if connection.is_connected():
            # print("Successfully connected to the database")
            # Create a cursor object
            cursor = connection.cursor()

            # Use parameterized query
            query = "SELECT Initials FROM F1_2023 WHERE Race_number = 1"
            cursor.execute(query)

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
            # print("MySQL connection is closed")
    
    return rows

def Select_driver(Race, Count):
    if __name__ == "__main__":
        
        print("********************************************** " + Race + " **********************************************************\n")

        print("Driver options are VER PER ALO SAI HAM STR RUS BOT GAS ALB TSU SAR MAG DEV HUL ZHO NOR OCO LEC PIA\n")
        
        # Get list of drivers from the database for this
        Driver_list = query_for_driver_list()

        print(Driver_list)
        
        # Set variables
        # No duplicate can be allowed. an if loop needed here, also check for correct formatting.
        Driver = "SAME"
        Driver_two = "SAME"

        while(Driver == Driver_two):
            print("Please select a different driver for each position. Use the drivers initials exactly as shown above")
            
            # while(len(Driver) != 3) or (Driver == Driver_two) or Driver != "VER" and Driver != "PER" and Driver != "ALO" and Driver != "SAI" and Driver != "HAM" and Driver != "STR" and Driver != "RUS" and Driver != "BOT" and Driver != "GAS" and Driver != "ALB" and Driver != "TSU" and Driver != "SAR" and Driver != "MAG" and Driver != "DEV" and Driver != "HUL" and Driver != "ZHO" and Driver != "NOR" and Driver != "OCO" and Driver != "LEC" and Driver != "PIA":
            while(len(Driver) != 3) or (Driver == Driver_two) and (Driver not in Driver_list):
               
                Driver = input("1st: ")
            while(len(Driver_two) != 3) or (Driver == Driver_two) or Driver_two != "VER" and Driver_two != "PER" and Driver_two != "ALO" and Driver_two != "SAI" and Driver_two != "HAM" and Driver_two != "STR" and Driver_two != "RUS" and Driver_two != "BOT" and Driver_two != "GAS" and Driver_two != "ALB" and Driver_two != "TSU" and Driver_two != "SAR" and Driver_two != "MAG" and Driver_two != "DEV" and Driver_two != "HUL" and Driver_two != "ZHO" and Driver_two != "NOR" and Driver_two != "OCO" and Driver_two != "LEC" and Driver_two != "PIA":
                Driver_two = input("2nd: ")

        Driver = Driver.upper()
        Driver_two = Driver_two.upper()

        print("\nYour selection is:\n1st: " + Driver + "\n2nd: " + Driver_two + "\n") 

        Choice = 'X'
        while (Choice != "N" and Choice != 'Y' and Choice != 'n' and Choice != 'y'):
            Choice = input("Enter Y to continue or N to change your selection: ")
        
        if Choice == 'Y' or Choice == 'y':
            results = query_with_variables(Count, Driver, Driver_two)
            print("Your score for this weeks race: " + str(results))
            
        else: results= Select_driver(Race, Count)
        # Return this weeks score
        return results
        
        

        

def main():
    # Player chooses name 
    player_name = Get_player_name()
    # Player chooses how many rounds to play
    race_amount = Choose_how_many_races()
    # This counts the race number we are currently at.
    Count = 0
    #  Counts the score for current race
    This_race_score  = 0
    # Counts total player score so far
    Overall_score = 0
    

    for i in race_amount:
        # i is the name of the curent race, count is the race number in the order. 
        Count += 1
        This_race_score = Select_driver(i, Count)
        Overall_score += This_race_score 
        print("\nYour current overall score is " + str(Overall_score))

    print("\nYour final score is " + str(Overall_score))
        
main()


