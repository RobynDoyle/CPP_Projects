from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random

# def Get_player_name(playername):
#     playername = playername.upper()
#     return playername


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    
    if request.method == 'POST':
        player_name = request.form['player_name'].upper()
        # player_name = 
        races = request.form['races']
        difficulty = request.form['difficulty']
        # Redirect to the select_driver page with player_name in the query string
        return redirect(url_for('select_driver', player_name=player_name, races=races, difficulty=difficulty))
    return render_template('start.html')

    
@app.route('/select_driver', methods=['GET'])
def select_driver():
    player_name = request.args.get('player_name')
    races = request.args.get('races')
    difficulty = request.args.get('difficulty')
    return render_template('select_driver.html', player_name=player_name, races=races, difficulty=difficulty)

# app.run(host="0.0.0.0", port=80)

if __name__ == '__main__':
    app.run(debug=True)