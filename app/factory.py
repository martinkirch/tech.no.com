from flask import Flask
from views import tcom


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static',
                )
    app.register_blueprint(tcom)
    return app
