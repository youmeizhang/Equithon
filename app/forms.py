from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class SignupForm(FlaskForm):
        full_name = StringField('Your Name', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign Up')


class ProfileForm(FlaskForm):
        school = StringField('School', validators=[DataRequired()])
        grade = StringField('Grade', validators=[DataRequired()])
        age = IntegerField('Age', validators=[DataRequired()])
        phone = IntegerField('Phone Number (optional)')
        address = StringField('Address (optional)')
        blurb = StringField('Tell Us About Yourself! (optional)')
        submit = SubmitField('Submit')