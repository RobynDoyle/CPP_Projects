from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random

# def Get_player_name(playername):
#     playername = playername.upper()
#     return playername


app = Flask(__name__)

def total_racesz():
    race_names = ["bahrain", "saudi-arabia", "australia", "azerbaijan", "miami", "monaco", "spain", "canada", "austria", "great-britain", "hungary", "belgium", "netherlands", "italy", "singapore", "japan", "qatar", "united-states", "mexico", "brazil", "las-vegas", "abu-dhabi"]
    races_uppercase_list = [item.upper() for item in race_names]
    return races_uppercase_list

def get_current_race(races, race_counter, total_races):
    
    Races_this_session = []
    
    for i in range(0,int(races)):
        Races_this_session.append(total_races[i])

    current_race = Races_this_session[race_counter]
    return current_race

def get_current_race_picture(race_counter):
    Races_picture = list(range(22))
    path_to_pic = url_for('static', filename=f'images/{Races_picture[race_counter]}.jpg')
    this_race_picture = path_to_pic
    return this_race_picture



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

def query_for_driver_list(Race_counter):
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
            cursor.execute(query, (Race_counter+1,))
            driver_list_out = cursor.fetchall()
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    Driver_clean_list = [driver[0] for driver in driver_list_out]
    return Driver_clean_list

def Select_driver(Race_counter):
    Driver_list = query_for_driver_list(Race_counter)
    return Driver_list


# ________________________________________FLASK PART_____________________________________________________________

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    

    race_counter = 0
    
    if request.method == 'POST':
        player_name = request.form['player_name'].upper()
        # player_name = 
        races = request.form['races']
        difficulty = request.form['difficulty']
        # Redirect to the select_driver page with player_name in the query string
        return redirect(url_for('select_driver', player_name=player_name, races=races, difficulty=difficulty, race_counter=race_counter))
    return render_template('start.html')


    
@app.route('/select_driver', methods=['GET', 'POST'])
def select_driver():
    if request.method == 'GET':
        race_counter = request.args.get('race_counter', type=int)
        races = request.args.get('races', type = int)
        player_name = request.args.get('player_name') #Shows playername
        difficulty = request.args.get('difficulty') #Outputs chose difficulty of this session
    elif request.method == 'POST':
        race_counter = request.form.get('race_counter', type=int)
        races = request.form.get('races', type=int)
        player_name = request.form.get('player_name')
        difficulty = request.form.get('difficulty')
        
    
  
    total_races = []
    total_races += total_racesz()
    
    

    if race_counter >= races:  # Check if race_counter reaches the number of races
        return render_template('end.html', player_name=player_name, races=races, difficulty=difficulty)


    driver_list = Select_driver(race_counter)
    
    current_race = get_current_race(races, race_counter, total_races) #Gets name of current race
    
    this_race_picture = get_current_race_picture(race_counter) #Gets different picture for each race
    
    
    # race_counter += 1 #Iterates for the next race
    
    return render_template('select_driver.html', race_counter=race_counter, player_name=player_name, races=races, difficulty=difficulty, current_race=current_race, this_race_picture=this_race_picture, driver_list=driver_list )
   
    
    # else: return render_template('end_game.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        race_counter = request.args.get('race_counter', type=int)
        races = request.args.get('races', type = int)
        player_name = request.args.get('player_name') #Shows playername
        difficulty = request.args.get('difficulty') #Outputs chose difficulty of this session
    elif request.method == 'POST':
        race_counter = request.form.get('race_counter', type=int)
        races = request.form.get('races', type=int)
        player_name = request.form.get('player_name')
        difficulty = request.form.get('difficulty')
    
    total_races = []
    total_races += total_racesz()
    driver_list = Select_driver(race_counter)
    
    current_race = get_current_race(races, race_counter, total_races) #Gets name of current race
    
    this_race_picture = get_current_race_picture(race_counter) #Gets different picture for each race
    race_counter += 1
    return render_template('result.html', race_counter=race_counter, player_name=player_name, races=races, difficulty=difficulty, current_race=current_race, this_race_picture=this_race_picture, driver_list=driver_list )


# app.run(host="0.0.0.0", port=80)

if __name__ == '__main__':
    app.run(debug=True)