from flask import Blueprint

tcom = Blueprint('tcom', __name__)


@tcom.route('/')
def home():
    return 'Hello, world'
