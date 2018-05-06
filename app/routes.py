from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from app.forms import SignupForm
from app.forms import ProfileForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lindsey'}
    posts = [
        #sample code
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You were successfully logged in')
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/userpage')
    return render_template('login.html', title='Login', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}, remember_me={}'.format(
            form.full_name.data, form.email.data))
        return redirect('/profile')
    return render_template('signup.html', title='Signup', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        return redirect('/userpage')
    return render_template('profile.html', title='Profile', form=form)


@app.route('/userpage')
def userpage():
    return render_template('userpage.html')

