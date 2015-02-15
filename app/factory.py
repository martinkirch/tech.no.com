from flask import Flask
from views import tcom


def create_app():
    app = Flask(__name__)
    app.register_blueprint(tcom)
    return app
