from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

class InputForm(FlaskForm):
    AREA_LIST = [('dl1', 'Development Line 1'),
            ('dl2', 'Development Line 2'),
            ('caf', 'Cafeteria')]

    HAZARD_LIST = [('fall', 'Fall Hazard'),
            ('shock', 'Electric Shock'),
            ('pierce', 'Piercing Hazard')]

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], default=datetime.utcnow)
    area = SelectField('Area/Equipment', choices=AREA_LIST, validators=[DataRequired()])
    location = StringField('Location')
    task = StringField('Location', validators=[DataRequired()])
    hazard = SelectField('Hazard', choices=HAZARD_LIST, validators=[DataRequired()])
    info = TextAreaField("Additional Information", validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class RegisterForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
