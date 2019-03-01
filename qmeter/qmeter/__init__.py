"""
The flask application package.
"""
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from qmeter.flaskdb import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

import qmeter.views
