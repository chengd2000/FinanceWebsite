from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .utils import login_user_handler, sign_in_user_handler, data_user_page_income, data_user_page_outcome

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_user_handler()
    return render_template('login.html', user=current_user)

@routes.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        return sign_in_user_handler()
    return render_template('sign_in.html', user=current_user)

@routes.route('/user_data', methods=['GET', 'POST'])
@login_required
def user_data():
    if request.method == 'POST':
        if 'income_amount' in request.form:
            return data_user_page_income()
        elif 'outcome_amount' in request.form:
            return data_user_page_outcome()
    return render_template('user_data.html', user=current_user)




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