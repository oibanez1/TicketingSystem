from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)



#Main Page
@app.route('/login' , methods=['GET' , 'POST'])
def login():
    return render_template('index.html')

#Register
@app.route('/login/register' , methods=['GET' , 'POST'])
def register():
    return

#Setup
@app.route('/setup')
def setup():
    return render_template('setup.html')

#Guest
@app.route('/guest')
@app.route('/guest/<name>')
def guest(name = None):
    return render_template('guest.html' , name = name)

#Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True)