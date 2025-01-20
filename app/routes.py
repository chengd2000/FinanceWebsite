from flask import Blueprint, json, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user
from .utils import login_user_handler, sign_in_user_handler, data_user_page_income, data_user_page_outcome
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_user_handler()
    return render_template('login.html', user=current_user)


@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))


@routes.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        print("in def sign in")
        return sign_in_user_handler()
    return render_template('sign_in.html', user=current_user)

@routes.route('/user_data', methods=['GET', 'POST'])
#@login_required
def user_data():
    if request.method == 'POST':
        if 'income_amount' in request.form:
            return data_user_page_income()
        elif 'outcome_amount' in request.form:
            return data_user_page_outcome()
    return render_template('user_data.html', user=current_user)




@routes.route('/delete-income', methods=['POST'])
def delete_income():  
    income = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    id = income['id']
    income = income.query.get(id)
    if income:
        if income.user_id == current_user.id:
            db.session.delete(income)
            db.session.commit()

    return jsonify({})


@routes.route('/delete-outcome', methods=['POST'])
def delete_outcome():  
    outcome = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    id = outcome['id']
    outcome = outcome.query.get(id)
    if outcome:
        if outcome.user_id == current_user.id:
            db.session.delete(outcome)
            db.session.commit()

    return jsonify({})