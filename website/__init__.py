from flask import Flask
import os
from dotenv import dotenv_values


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = dotenv_values(".env")['SECRET_KEY']

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    return app
