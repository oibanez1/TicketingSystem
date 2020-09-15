from flask import render_template, request, redirect, url_for, session
from app.__init__ import app
from app.forms import LoginForm

#Main Page
@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('/dashboard'))
    return render_template('index.html' , form=form)

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