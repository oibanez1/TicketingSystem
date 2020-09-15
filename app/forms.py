from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Username' , validators=[DataRequired()])
    password = PasswordField('Password' , validators=[DataRequired()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired()])
    password = PasswordField('Password' , validators=[DataRequired()])
    create = SubmitField('Create')

# class TicketForm(FlaskForm):
    