from flask import Blueprint, render_template, request, jsonify
import requests

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@main.route('/user_data')
def user_data():
    return render_template('user_data.html')