from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

# app.run(host="0.0.0.0", port=80)

if __name__ == '__main__':
    app.run(debug=True)