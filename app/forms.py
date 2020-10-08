from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models.models import User

class LoginForm(FlaskForm):
    email = StringField('Username' , validators=[DataRequired()])
    password = PasswordField('Password' , validators=[DataRequired()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    create = SubmitField('Create')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            print("Already Exists")
            raise ValidationError('Email already registered here')    

# class TicketForm(FlaskForm):
    