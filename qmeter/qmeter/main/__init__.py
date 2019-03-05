from flask import Blueprint

bp = Blueprint('main', __name__)

from qmeter.main import routes