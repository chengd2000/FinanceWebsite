from flask import Blueprint, flash, redirect, url_for, request, current_app
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Income, Outcome
from . import db

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

    if not amount or not category or not date:
        flash('All fields are required!', category='error')
    else:
        new_income = Income(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_income)
        db.session.commit()
        flash('Income added!', category='success')

    return redirect(url_for('routes.user_data'))

@utils.route('/outcome', methods=['POST'])
def data_user_page_outcome():
    amount = request.form.get('outcome_amount')
    details = request.form.get('details_outcome')
    category = request.form.get('category_outcome')
    date = request.form.get('date_outcome')

    if not amount or not category or not date:
        flash('All fields are required!', category='error')
    else:
        new_outcome = Outcome(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_outcome)
        db.session.commit()
        flash('Outcome added!', category='success')

    return redirect(url_for('routes.user_data'))

@utils.route('/login', methods=['POST'])
def login_user_handler():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('routes.user_data'))
    else:
        flash('Incorrect username/password, try again.', category='error')
        return redirect(url_for('routes.login'))

@utils.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@utils.route('/sign_in', methods=['POST'])
def sign_in_user_handler():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    password_again = request.form.get('password_again')

    if User.query.filter_by(email=email).first():
        flash('Email already exists.', category='error')
    elif len(email) < 4 or len(username) < 2 or len(password) < 7:
        flash('Invalid input data.', category='error')
    elif password != password_again:
        flash('Passwords don\'t match.', category='error')
    else:
        new_user = User(email=email, username=username,
                        password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        return redirect(url_for('routes.user_data'))

    return redirect(url_for('routes.sign_in'))

