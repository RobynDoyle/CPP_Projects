import mysql.connector
from mysql.connector import Error

# Gets players name for the game.
def Get_player_name():
    print("**************************************** PLAYER DETAILS ********************************************************\n")
    print("Enter your name and get ready to play!")
    
    playername = input("Enter player name: ")
    playername = playername.upper()
    print("Your player name is: " + playername + "\n")

    return playername 

# Runs the query to the database for race names of this season, after user defines how many are needed
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

# Runs the query to the database for driver data
def query_with_variables(Count, Driver, Driver_two, Driver_three):
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
            query = "SELECT Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Count, Driver, Count, Driver_two, Count, Driver_three))

            # Fetch the results
            rows = cursor.fetchall()

            # Print the results
            # for row in rows:
            #     print(row)

            # Close the cursor
            # cursor.close()


            # Print the drivers name beside their score
            query = "SELECT Position, Last_name, Car, Laps, Time, Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Count, Driver, Count, Driver_two, Count, Driver_three))

            # Fetch the results
            display_rows = cursor.fetchall()

            # Print the results
            for row in display_rows:
                print(str(row[1]) + ": Finishing position = " + str(row[0]) + ". Team = " + str(row[2]) + ". Laps completed = " + str(row[3]) + ". Time = " + str(row[4])  + ". Points " + str(row[5]) + "\n")

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

# This function queries the database for the list of drivers that raced in current race. List changes every time.
def query_for_driver_list(Count):
    
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
            query = "SELECT Initials FROM F1_2023 WHERE (Race_number = %s)"
            cursor.execute(query, (Count,))

            # Fetch the results
            driver_list_out = cursor.fetchall()

            # for row in rows:
            #     print(row)

            # Close the cursor
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            # Close the connection
            connection.close()
            # print("MySQL connection is closed")
    
    return driver_list_out

# This function gets the player's driver choice and asks the database for the points that the drivers scored
def Select_driver(Race, Count):
    if __name__ == "__main__":
        
        print("********************************************** " + Race + " **********************************************************\n")

        #  print("Driver options are VER PER ALO SAI HAM STR RUS BOT GAS ALB TSU SAR MAG DEV HUL ZHO NOR OCO LEC PIA\n")
        
        # Get list of drivers from the database for this
        Driver_list = query_for_driver_list(Count)
        Driver_clean_list = []
      
        # Output driver lists from the SQL query needs to be converted to a single list, using range of the length of driver list, changes with each race.     
        for i in range (0,len(Driver_list)):
            x = Driver_list[i][0]
            Driver_clean_list.append(x)

        print("Driver options are " + str(Driver_clean_list))

        #  Driver variables pre set    
        Driver = "SAME"
        Driver_two = "SAME"
        Driver_three = "SAME"

        # Driver selection
        print("Please select a different driver for each podium position. Use the drivers initials in this exact 3 letter format -> ROB")

        while (Driver not in Driver_clean_list): 
            Driver = input("1st: ")
            Driver = Driver.upper()
        while (Driver == Driver_two) or (Driver_two not in Driver_clean_list):
            Driver_two = input("2nd: ")
            Driver_two = Driver_two.upper()
        while (Driver_three == Driver_two) or (Driver_three == Driver) or (Driver_three not in Driver_clean_list):
            Driver_three = input("3rd: ")
            Driver_three = Driver_three.upper()

        

        print("\nYour selection is:\n1st: " + Driver + "\n2nd: " + Driver_two + "\n3rd: " + Driver_three + "\n") 
        
        # allows user to end game now
        exit_choice = 'N'
        Choice = 'X'
        while (Choice != 'N' and Choice != 'Y' and Choice != 'n' and Choice != 'y' and Choice != 'E' and Choice != 'e'):
            Choice = input("Enter Y to continue, N to change your selection or E to exit game: ")
            
        
        if Choice == 'Y' or Choice == 'y' or Choice == 'E' or Choice == 'e':
            print(" ")
            results = query_with_variables(Count, Driver, Driver_two, Driver_three)
            print("Your score for this weeks race: " + str(results)) 

            return results, Choice
        # else if: Choice == 'E' or 
        # Else Re run the select driver funciton, and then return the final grade 
        else: results, Choice = Select_driver(Race, Count) 

        # return results, Choice
        # Return this weeks score
        

        return results, Choice
        
# Houses main programm calls        
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
        This_race_score, end_game_maybe = Select_driver(i, Count)
        Overall_score += This_race_score
        
        # Overall_score += This_race_score[0] 
        print("\n" + player_name + "'s current overall score is " + str(Overall_score))

        # If player chose E then exit game
        if end_game_maybe == 'E' or end_game_maybe == 'e':
                break
        

    print("\n" + player_name + "'s final score is " + str(Overall_score))
    print("Thank you " + player_name + " for playing!")
        
main()


