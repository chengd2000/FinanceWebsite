from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .utils import *

routes = Blueprint('routes', __name__)  # שינה את השם מ-main ל-routes

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    login_user(request)
    return render_template('login.html', user=current_user)

@routes.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    sign_in_user(request)
    return render_template('sign_in.html', user=current_user)

@routes.route('/user_data', methods=['GET', 'POST'])
def user_data():
    data_user_page_income(request)
    data_user_page_outcome(request)
    return render_template('user_data.html')



# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})