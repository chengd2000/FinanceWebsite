from datetime import datetime
from flask import Blueprint, Flask, flash, json, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user
from .utils import change_password, convert_to_dict, filter_data, forgot_password, login_user_handler, sign_in_user_handler, data_user_page_income, data_user_page_outcome
from . import db
from .models import Income, Outcome, PasswordResetForm, PasswordResetRequestForm, User  # Adjust the import based on your project structure
import calendar
from flask_mail import Mail, Message

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    if 'username' in request.form:
        return login_user_handler()
    elif 'email_forgot' in request.form:
        return forgot_password()
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
@login_required
def user_data():
    income = request.args.get('income', '')
    outcome = request.args.get('outcome', '')
    viewer=request.args.get('viewBy', '')
    amount = request.args.get('amount', '')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    category = request.args.get('category', '')
    if request.method == 'POST':
        if 'income_amount' in request.form:
            return data_user_page_income()
        elif 'outcome_amount' in request.form:
            return data_user_page_outcome()
        elif 'amount_filter' in request.form:
            return filter_data()
        
        
    
        else:
            return change_password()



# Sample data
    temp = [
        {'items': current_user.incomes, 'inOrOut': 'income'},
        {'items': current_user.outcomes, 'inOrOut': 'outcome'}
    ]

    sum=0

    # Merging items into a single list with 'inOrOut' field
    merged = [
        convert_to_dict(item, temp[0]['inOrOut']) for item in temp[0]['items']
    ] + [
        convert_to_dict(item, temp[1]['inOrOut']) for item in temp[1]['items']
    ]
    onlyIns=[convert_to_dict(item, temp[0]['inOrOut']) for item in temp[0]['items']]
    onlyOuts=[convert_to_dict(item, temp[1]['inOrOut']) for item in temp[1]['items']]
    
    # Creating the result list based on conditions
    res = []

    if income == 'true' and outcome == 'true':
        res = merged
    elif income == 'true':
        res = onlyIns
    elif outcome == 'true':
        res = onlyOuts

    # Sorting the result list by the 'date' field
    res = sorted(res, key=lambda x: x['date'] if isinstance(x['date'], datetime) else datetime.strptime(x['date'], "%Y-%m-%d"))
    if(viewer=='amount'):
        res = sorted(res, key=lambda x: x['amount'], reverse=True)
    for item in merged:
        if item['inOrOut']=='income':
            sum+=item['amount']
        else:
            sum-=item['amount']

    # if(filter=='date'):



    sum_of_year = [0, 0, 0, 0, 0, 0]
    income_of_year = [0, 0, 0, 0, 0, 0]
    outcome_of_year = [0, 0, 0, 0, 0, 0]
    for item in merged:
        if str(item['date'].year) == '2020': 
            if item['inOrOut']=='income':
                sum_of_year[0]+=item['amount']
                income_of_year[0] += item['amount']
            else:
                sum_of_year[0]-=item['amount']
                outcome_of_year[0] += item['amount']

        if str(item['date'].year) == '2021': 
            if item['inOrOut']=='income':
                sum_of_year[1]+=item['amount']
                income_of_year[1] += item['amount']
            else:
                sum_of_year[1]-=item['amount']
                outcome_of_year[1] += item['amount']

        if str(item['date'].year) == '2022': 
            if item['inOrOut']=='income':
                sum_of_year[2]+=item['amount']
                income_of_year[2] += item['amount']
            else:
                sum_of_year[2]-=item['amount']
                outcome_of_year[2] += item['amount']

        if str(item['date'].year) == '2023': 
            if item['inOrOut']=='income':
                sum_of_year[3]+=item['amount']
                income_of_year[3] += item['amount']
            else:
                sum_of_year[3]-=item['amount']
                outcome_of_year[3] += item['amount']

        if str(item['date'].year) == '2024': 
            if item['inOrOut']=='income':
                sum_of_year[4]+=item['amount']
                income_of_year[4] += item['amount']
            else:
                sum_of_year[4]-=item['amount']
                outcome_of_year[4] += item['amount']

        if str(item['date'].year) == '2025': 
            if item['inOrOut']=='income':
                sum_of_year[5]+=item['amount']
                income_of_year[5] += item['amount']
            else:
                sum_of_year[5]-=item['amount']   
                outcome_of_year[5] += item['amount']  


                                                

    max_income=0
    max_income_category=""
    max_income_date=""
    for item in onlyIns:
        if item['amount']>max_income:
            max_income=item['amount']
            max_income_category=item['category']
            max_income_date = calendar.month_name[item['date'].month] + ", " + str(item['date'].year)
    
    max_outcome=0
    max_outcome_category=""
    max_outcome_date=""
    for item in onlyOuts:
        if item['amount']>max_outcome:
            max_outcome=item['amount']
            max_outcome_category=item['category']
            max_outcome_date = calendar.month_name[item['date'].month] + ", " + str(item['date'].year)
    # עדכון temp עם הרשימה הממוינת
    print(res)


    outcome_by_category = [0, 0]
    for item in onlyOuts:
        if item['category'] == 'Food':
            outcome_by_category[0] += 1
        if item['category'] == 'Rent':
            outcome_by_category[1] += 1    

    income_by_category = [0, 0, 0]
    for item in onlyIns:
        if item['category'] == 'Salary':
            income_by_category[0] += 1
        if item['category'] == 'Investments':
            income_by_category[1] += 1  
        if item['category'] == 'Business':
            income_by_category[2] += 1           

    arr = []
    for i in res:
        is_valid = True
        if amount != '':
            is_valid &= i['amount'] >= int(amount)
        if category != '':
            is_valid &= i['category'] == category
        if date_to != '':
            is_valid &= i['date'] <= datetime.strptime(date_to, "%Y-%m-%d")
        if date_from != '':
            is_valid &= i['date'] >= datetime.strptime(date_from, "%Y-%m-%d")
        
        if is_valid:
            arr.append(i)
 

    unique_array = []
    for item in arr:
        if item not in unique_array:
            unique_array.append(item)             

    res = unique_array                

    for k in res:
        k['date'] = str(k['date'].day) + '/' + str(k['date'].month) + '/' + str(k['date'].year)

    

    return render_template('user_data.html',income='true',outcome='true', user=current_user, temp=res,sum=sum,max_income=max_income,max_income_category=max_income_category,max_income_date=max_income_date,max_outcome=max_outcome,max_outcome_category=max_outcome_category,max_outcome_date=max_outcome_date, sum_of_year=sum_of_year, outcome_by_category=outcome_by_category, income_by_category=income_by_category, income_of_year=income_of_year, outcome_of_year=outcome_of_year)



@routes.route('/delete-income', methods=['POST'])
def delete_income():  
    try:
        income_data = json.loads(request.data)  # this function expects a JSON from the INDEX.js file 
        id = income_data['id']
        income = Income.query.get(id)
        if income and income.user_id == current_user.id:
            db.session.delete(income)
            db.session.commit()
            return jsonify({"success": True})
        else:
            return jsonify({"error": "Income not found or unauthorized"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/delete-outcome', methods=['POST'])
def delete_outcome():  
    try:
        outcome_data = json.loads(request.data)  # this function expects a JSON from the INDEX.js file 
        id = outcome_data['id']
        outcome = Outcome.query.get(id)
        if outcome and outcome.user_id == current_user.id:
            db.session.delete(outcome)
            db.session.commit()
            return jsonify({"success": True})
        else:
            return jsonify({"error": "Outcome not found or unauthorized"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500




