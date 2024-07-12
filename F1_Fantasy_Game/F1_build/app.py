from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random

# def Get_player_name(playername):
#     playername = playername.upper()
#     return playername


app = Flask(__name__)

def get_current_race(races, race_counter):
    
    race_names = ["bahrain", "saudi-arabia", "australia", "azerbaijan", "miami", "monaco", "spain", "canada", "austria", "great-britain", "hungary", "belgium", "netherlands", "italy", "singapore", "japan", "qatar", "united-states", "mexico", "brazil", "las-vegas", "abu-dhabi"]
    races_uppercase_list = [item.upper() for item in race_names]

    Races_this_session = []

    for i in range(0,races):
        Races_this_session.append(races_uppercase_list[i])

    current_race = Races_this_session[race_counter]
    return current_race


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

    
@app.route('/select_driver', methods=['GET'])
def select_driver():
    race_counter = request.args.get('race_counter')
    races = request.args.get('races')
    
    while race_counter < races:
        race_counter += 1
        player_name = request.args.get('player_name')
        
        current_race = get_current_race(races, race_counter)
        difficulty = request.args.get('difficulty')
        return render_template('select_driver.html', player_name=player_name, races=races, difficulty=difficulty,  current_race=current_race)

# app.run(host="0.0.0.0", port=80)

if __name__ == '__main__':
    app.run(debug=True)