from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)  # name of module running to create app
    app.config['SECRET_KEY'] = "helloworld"

    from .views import views
    from .auth import auth
    
    app. register_blueprint(views, url_prefix="/")
    app. register_blueprint(views, url_prefix="/")
    
    return app
