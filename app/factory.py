from flask import Flask
from flask.ext.xstatic import FlaskXStatic
from views import tcom


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static',
                )
    xs = FlaskXStatic(app)
    xs.add_module('bootstrap')
    app.register_blueprint(tcom)
    return app
