from flask import Flask,render_template,request,redirect
from flask_ngrok import run_with_ngrok
from db import Database

app = Flask(__name__)

run_with_ngrok(app)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods =['post'])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_mail")
    password = request.form.get("user_password")
    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html', message="Registration Successful.Kindly login to proceed")

    else:
        return render_template('register.html',message="Email Already Exist")


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return "Incorrect email or password"



@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/Python')
def python():
    return render_template('python.html')

@app.route('/Data Science')
def data_science():
    return render_template('data_science.html')

@app.route('/Course_Content')
def Course_Content():
    return render_template('Course_Content.html')

@app.route('/Data Analytics')
def Data_Analytics():
    return render_template('Data_Analytics.html')
@app.route('/Web Development')
def Web_Development():
    return render_template('Web_Development.html')


app.run()