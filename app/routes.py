from flask import Blueprint, render_template, request, jsonify
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from .utils import *

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login')
def login():
    login_user()
    return render_template('login.html', user=current_user)


@main.route('/sign_in')
def sign_in():
    sign_in_user()
    return render_template('sign_in.html', user=current_user)


@main.route('/user_data')
def user_data():
    data_user_page_income()
    data_user_page_outcome()
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