from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Income, Outcome
from .__init__ import db

# הגדרת ה-Blueprint
utils = Blueprint('utils', __name__)

# פונקציה לטיפול בהכנסות
@utils.route('/income', methods=['POST'])
def data_user_page_income():
    from . import db  # ייבוא מקומי של db בתוך הפונקציה כדי למנוע מעגל ייבוא

    amount = request.form.get('income_amount')
    details = request.form.get('details_income')
    category = request.form.get('category_income')
    date = request.form.get('date_income')

    if len(amount) < 1:
        flash('amount is empty!', category='error')
    if len(category) < 1:
        flash('category is empty!', category='error')
    if len(date) < 1:
        flash('date is empty!', category='error')

    else:
        new_income = Income(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_income)
        db.session.commit()
        flash('Income added!', category='success')

# פונקציה לטיפול בהוצאות
@utils.route('/outcome', methods=['POST'])
def data_user_page_outcome():
    from . import db  # ייבוא מקומי של db בתוך הפונקציה כדי למנוע מעגל ייבוא

    amount = request.form.get('outcome_amount')
    details = request.form.get('details_outcome')
    category = request.form.get('category_outcome')
    date = request.form.get('date_outcome')

    if len(amount) < 1:
        flash('amount is empty!', category='error')
    if len(category) < 1:
        flash('category is empty!', category='error')
    if len(date) < 1:
        flash('date is empty!', category='error')

    else:
        new_outcome = Outcome(amount=amount, details=details, category=category, date=date, user_id=current_user.id)
        db.session.add(new_outcome)
        db.session.commit()
        flash('Outcome added!', category='success')

# פונקציה להתחברות של המשתמש
@utils.route('/login', methods=['POST'])
def login_user_custom(request):
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

# פונקציה להתנתקות
@utils.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.html'))

# פונקציה לרישום משתמש חדש
@utils.route('/signup', methods=['POST'])
def sign_in_user(request):
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
            new_user = User(email=email, username=username,
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('utils.user_data'))
