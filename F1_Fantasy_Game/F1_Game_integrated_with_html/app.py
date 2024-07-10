from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random
import time

app = Flask(__name__)

def Get_player_name(playername):
    playername = playername.upper()
    return playername

def Choose_how_many_races(races):
    races_int = int(races)
    races_amount = [i for i in range(1, races_int + 1)]
    race_names = ["bahrain", "saudi-arabia", "australia", "azerbaijan", "miami", "monaco", "spain", "canada", "austria", "great-britain", "hungary", "belgium", "netherlands", "italy", "singapore", "japan", "qatar", "united-states", "mexico", "brazil", "las-vegas", "abu-dhabi"]
    races_uppercase_list = [item.upper() for item in race_names]
    Races_this_session = races_uppercase_list[:races]
    return Races_this_session

def Choose_difficulty(difficulty):
    Difficulty = difficulty.upper()
    if Difficulty == "HARD":
        Difficulty_number = 14
    elif Difficulty == "MEDIUM":
        Difficulty_number = 10
    else:
        Difficulty_number = 6
    return Difficulty_number

def query_with_variables(Count, Driver, Driver_two, Driver_three):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Count, Driver, Count, Driver_two, Count, Driver_three))
            rows = cursor.fetchall()
            query = "SELECT Position, Last_name, Car, Laps, Time, Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (Count, Driver, Count, Driver_two, Count, Driver_three))
            display_rows = cursor.fetchall()
            print("--------------------------------------------------------------------------------------------------------------")
            for row in display_rows:
                print(str(row[1]) + ": Finishing position = " + str(row[0]) + ". Team = " + str(row[2]) + ". Laps completed = " + str(row[3]) + ". Time = " + str(row[4]) + ". Points " + str(row[5]) + "\n")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    points_counter = 0
    for tup in rows:
        points_counter += sum(tup)
    return points_counter

def query_for_driver_list(Count):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT Initials FROM F1_2023 WHERE (Race_number = %s)"
            cursor.execute(query, (Count,))
            driver_list_out = cursor.fetchall()
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    Driver_clean_list = [driver[0] for driver in driver_list_out]
    return Driver_clean_list

def Select_driver(Race, Count):
    Driver_list = query_for_driver_list(Count)
    Driver = "SAME"
    Driver_two = "SAME"
    Driver_three = "SAME"
    return Driver_list

def AI_Select_driver(Count, Difficulty):
    Driver_list = query_for_driver_list(Count)
    AI_DRIVER_one = "SAME"
    AI_DRIVER_two = "SAME"
    AI_DRIVER_three = "SAME"
    while (AI_DRIVER_one not in Driver_list): 
        pick_one = random.randint(0, (len(Driver_list)-Difficulty))
        AI_DRIVER_one = Driver_list[pick_one]
        AI_DRIVER_one= AI_DRIVER_one.upper()
    while (AI_DRIVER_two not in Driver_list) or (AI_DRIVER_two == AI_DRIVER_one): 
        pick_two = random.randint(0, (len(Driver_list)-Difficulty))
        AI_DRIVER_two = Driver_list[pick_two]
        AI_DRIVER_two= AI_DRIVER_two.upper()
    while (AI_DRIVER_three not in Driver_list) or (AI_DRIVER_three == AI_DRIVER_one) or (AI_DRIVER_three == AI_DRIVER_two): 
        pick_three = random.randint(0, (len(Driver_list)-Difficulty))
        AI_DRIVER_three = Driver_list[pick_three]
        AI_DRIVER_three= AI_DRIVER_three.upper()
    AI_results = query_with_variables(Count, AI_DRIVER_one, AI_DRIVER_two, AI_DRIVER_three)
    print("AI's Score for this race is " + str(AI_results))
    return AI_results

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    player_name = request.form.get('player_name')
    races = int(request.form.get('races'))
    difficulty = request.form.get('difficulty')
    player_name = Get_player_name(player_name)
    races_this_session = Choose_how_many_races(races)
    difficulty_number = Choose_difficulty(difficulty)
    count = 0
    overall_score = 0
    ai_overall_score = 0
    for race in races_this_session:
        count += 1
        driver_list = Select_driver(race, count)
        return render_template('select_driver.html', player_name=player_name, race=race, driver_list=driver_list)
    return redirect(url_for('home'))

@app.route('/select_driver', methods=['POST'])
def select_driver():
    race = request.form.get('race')
    count = int(request.form.get('count'))
    driver = request.form.get('driver')
    driver_two = request.form.get('driver_two')
    driver_three = request.form.get('driver_three')
    results = query_with_variables(count, driver, driver_two, driver_three)
    ai_results = AI_Select_driver(count, difficulty)
    overall_score += results
    ai_overall_score += ai_results
    return render_template('results.html', player_name=player_name, race=race, results=results, ai_results=ai_results, overall_score=overall_score, ai_overall_score=ai_overall_score)

if __name__ == '__main__':
    app.run(debug=True)
