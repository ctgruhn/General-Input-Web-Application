from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SelectField, TextAreaField, DateField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hazardapp import app, db, bcrypt
from hazardapp.models import User
from hazardapp.config import AREA_LIST, HAZARD_LIST
from datetime import datetime

class InputForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], default=datetime.utcnow)
    area = SelectField('Area/Equipment', choices=[(area_key, area_value) for area_key, area_value in AREA_LIST.items()], validators=[DataRequired()])
    location = StringField('Location')
    task = StringField('Task', validators=[DataRequired()])
    hazard = SelectField('Hazard', choices=[(hazard_key, hazard_value) for hazard_key, hazard_value in HAZARD_LIST.items()], validators=[DataRequired()])
    details = TextAreaField("Additional Information", validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please try again.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already being used. Please try again.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
