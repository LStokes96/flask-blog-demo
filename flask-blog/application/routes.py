from flask import render_template
from application import app

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About', desc="This is about blogs")

@app.route('/login')
def login():
    return render_template('login.html',title='Login', desc="Log in:")

@app.route('/register')
def register():
    return render_template('register.html',title='Register', desc="Register Here:")
