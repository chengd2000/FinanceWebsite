from flask import Blueprint, flash, redirect, url_for, request, current_app
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Income, Outcome
from . import db
from datetime import datetime
from sqlalchemy import create_engine, update 
from sqlalchemy.orm import sessionmaker

utils = Blueprint('utils', __name__)

# פונקציה לבדוק האם הדאטה בייס ריק ולהציג את המשתמשים
def check_if_database_empty():
    all_users = User.query.all()
    if not all_users:
        current_app.logger.info("The database is empty. No users found.")
        print("The database is empty. No users found.")
    else:
        current_app.logger.info(f"Found {len(all_users)} user(s) in the database:")
        print(f"Found {len(all_users)} user(s) in the database:")
        for user in all_users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

# דוגמא לקריאה לפונקציה (אפשר למחוק או להשאיר לצורכי בדיקות)
@utils.route('/check_database', methods=['GET'])
def check_database_handler():
    check_if_database_empty()
    flash('Database check complete. Check the logs or console for details.', category='info')
    return redirect(url_for('routes.home'))

@utils.route('/income', methods=['POST'])
def data_user_page_income():
    amount = request.form.get('income_amount')
    details = request.form.get('details_income')
    category = request.form.get('category_income')
    date = request.form.get('date_income')
    print(" היחהו איזה עצבים")

    if not amount or not category or not date:
        flash('All fields are required!', category='error')
    else:
        # המרת תאריך
        date = datetime.strptime(date, '%Y-%m-%d').date()
        new_income = Income(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_income)
        db.session.commit()
        flash('Income added!', category='success')
        print("איזה עצבים")

    return redirect(url_for('routes.user_data',income='true',outcome='false',viewBy='date', amount='', date_from='1900-01-01', date_to='', category=''))

@utils.route('/outcome', methods=['POST'])
def data_user_page_outcome():
    amount = request.form.get('outcome_amount')
    details = request.form.get('details_outcome')
    category = request.form.get('category_outcome')
    date = request.form.get('date_outcome')

    if not amount or not category or not date:
        flash('All fields are required!', category='error')
    else:
        # המרת תאריך
        date = datetime.strptime(date, '%Y-%m-%d').date()
        new_outcome = Outcome(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_outcome)
        db.session.commit()
        flash('Outcome added!', category='success')

    return redirect(url_for('routes.user_data',income='false',outcome='true',viewBy='date', amount='', date_from='1900-01-01', date_to='', category=''))

@utils.route('/login', methods=['POST'])
def login_user_handler():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user and (user.password == password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('routes.user_data',income='true',outcome='true',viewBy='date', amount='', date_from='1900-01-01', date_to='', category=''))
    else:
        flash('Incorrect username/password, try again.', category='error')
        return redirect(url_for('routes.login'))


@utils.route('/sign_in', methods=['POST'])
def sign_in_user_handler():
    print(1)
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    password_again = request.form.get('password_again')

    print(2)
    if User.query.filter_by(username=username).first():
        flash('Username already exists.', category='error')
    elif len(email) < 4 or len(username) < 2:
        flash('Invalid input data.', category='error')
    elif password != password_again:
        flash('Passwords don\'t match.', category='error')
    else:
        print(3)
        new_user = User(username=username, email=email, 
                        password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            print("User added successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
        print(4)
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        # return "5"
        return redirect(url_for('routes.user_data',income='true',outcome='true',viewBy='date', amount='', date_from='1900-01-01', date_to='', category=''))

    print(250)
    return redirect(url_for('routes.sign_in'))


def change_password():
    password_new = request.form.get('password')
    if current_user.password != password_new:
        db.session.execute(update(User).where(User.id == current_user.id).values(password=password_new)) 
        db.session.commit()
    return redirect(url_for('routes.user_data',income='true',outcome='true',viewBy='date', amount='', date_from='1900-01-01', date_to='', category=''))
# Function to convert custom objects to dictionaries
def convert_to_dict(item, inOrOut):
    return {
        'id':item.id,
        'date': item.date,
        'amount': item.amount,
        'category':item.category,
        'details':item.details,
        'inOrOut': inOrOut
    }


def filter_data():
    amount = request.form.get('amount_filter')
    date_from = request.form.get('date_filter_from')
    date_to = request.form.get('date_filter_to')
    category = request.form.get('category_filter')

    return redirect(url_for('routes.user_data',income='true',outcome='true',viewBy='date', amount=amount, date_from=date_from, date_to=date_to, category=category))