from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # ייבוא והגדרת Blueprints
    from .utils import utils
    from .routes import routes

    # רישום Blueprints
    app.register_blueprint(utils, url_prefix='/utils')
    app.register_blueprint(routes, url_prefix='/')

    # יצירת בסיס הנתונים אם הוא לא קיים
    from .models import User, Income, Outcome
    with app.app_context():
        db.create_all()

    # הגדרת LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


