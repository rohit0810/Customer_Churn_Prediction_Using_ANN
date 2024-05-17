from flask import Flask, render_template, request, redirect, session
from db import Database
import api
import os
import numpy as np

app = Flask(__name__)
app.secret_key = os.urandom(24)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    if session:
        # Extracting form data
        credit_score = float(request.form.get('cs'))
        age = int(request.form.get('age'))
        tenure = int(request.form.get('tenure'))
        balance = float(request.form.get('balance'))
        num_of_products = int(request.form.get('nop'))
        has_cr_card = int(request.form.get('hcc'))
        is_active_member = int(request.form.get('active'))
        estimated_salary = float(request.form.get('ES'))
        is_german = int(request.form.get('german'))
        is_spanish = int(request.form.get('spain'))
        is_male = int(request.form.get('male'))


        # Combine the extracted data into a dictionary or another suitable format
        data = np.array([
            [
                credit_score, age, tenure, balance, num_of_products,
                has_cr_card, is_active_member, estimated_salary,
                is_german, is_spanish, is_male
            ]
        ])

        # Pass the data to the API for prediction
        response = api.prediction(data)

        return render_template('profile.html', response=response)
    else:
        return redirect('/')

app.run(debug=True)