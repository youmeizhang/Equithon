from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class SignupForm(FlaskForm):
        first_name = StringField('Your Name', validators=[DataRequired()])
        last_name = StringField('Your Name', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign Up')


class ProfileForm(FlaskForm):
        school = StringField('Your Name', validators=[DataRequired()])
        grade = StringField('Grade', validators=[DataRequired()])
        age = StringField('Age', validators=[DataRequired()])
        phone = IntegerField('Phone Number (optional)')
        address = StringField('Address (optional)')
        subjects = SelectField('Subjects', validators=[DataRequired()])
        avail_days = SelectField('Available Days of the Week', validators=[DataRequired()])
        blurb = StringField('Tell Us About Yourself! (optional)')
        submit = SubmitField('Submit')