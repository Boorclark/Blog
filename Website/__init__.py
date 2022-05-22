from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # db path using flask sql
    db.init_app(app) # initialize db with flask app
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User # import all models before creating database

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" # if not logged in redirect user to this
    login_manager.init_app(app)

    @login_manager.user_loader # uses session (from my understanding like a temporary cache) of a user that is logged in
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME): # checks if path exists
        db.create_all(app=app) # if not -> create
        print("Created database!")