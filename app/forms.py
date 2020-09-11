from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Data_Required

class LoginForm(FlaskForm):
    email = StringField('Username' , validators=[Data_Required()])
    password = PasswordField('Password' , validators=[Data_Required()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email' , validators=[Data_Required()])
    password = PasswordField('Password' , validators=[Data_Required()])
    create = SubmitField('Create')

class TicketForm(FlaskForm):
    