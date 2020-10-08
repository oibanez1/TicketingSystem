from flask import render_template, request, redirect, url_for, session, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.__init__ import app
from app.forms import LoginForm, RegisterForm
from app.models.models import User
from app.__init__ import db

#Main Page
@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_pass(form.password.data):
            print("invalid")
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('dashboard')
        return redirect(next_page)
        # flash('Login requested for user {}'.format(form.email.data))
    return render_template('index.html' , form=form)

#Register
@app.route('/register' , methods=['GET' , 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        print('yay, Now Registered')
        return redirect(url_for('login'))
    return render_template('register.html' , form=form)

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
@login_required
def dashboard():
    return render_template('dashboard.html')

#logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))