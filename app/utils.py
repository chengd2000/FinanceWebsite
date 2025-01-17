from flask import redirect, request, url_for
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Income, Outcome
from . import db
import json
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user



def data_user_page_income():
    
    if request.method == 'POST': 
        amount = request.form.get('income_amount')
        details = request.form.get('details_income')#Gets the note from the HTML 
        category = request.form.get('category_income')
        date = request.form.get('date_income')
        

        if len(amount) < 1:
            flash('amount is empty!', category='error') 
        if len(category) < 1:
            flash('category is empty!', category='error') 
        if len(date) < 1:
            flash('date is empty!', category='error') 

        else:
            new_income = Income(amount = amount, details = details, category = category, date = date, user_id = current_user.id)  #providing the schema for the note 
            db.session.add(new_income) #adding the note to the database 
            db.session.commit()
            flash('Income added!', category='success')


def data_user_page_outcome():
    
    if request.method == 'POST': 
        amount = request.form.get('outcome_amount')
        details = request.form.get('details_outcome')#Gets the note from the HTML 
        category = request.form.get('category_outcome')
        date = request.form.get('date_outcome')
        

        if len(amount) < 1:
            flash('amount is empty!', category='error') 
        if len(category) < 1:
            flash('category is empty!', category='error') 
        if len(date) < 1:
            flash('date is empty!', category='error') 

        else:
            new_outcome = Outcome(amount = amount, details = details, category = category, date = date, user_id = current_user.id)  #providing the schema for the note 
            db.session.add(new_outcome) #adding the note to the database 
            db.session.commit()
            flash('Outcome added!', category='success')


def login_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('utils.user_data'))
            else:
                flash('Incorrect username/password, try again.', category='error')
        else:
            flash('Incorrect username/password, try again.', category='error')


@login_required
def logout():
    logout_user()
    return redirect(url_for('index.html'))


def sign_in_user():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_again = request.form.get('password_again')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password != password_again:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('utils.user_data'))




