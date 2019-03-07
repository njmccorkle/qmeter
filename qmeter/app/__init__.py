from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import json
#import time
#from datetime import datetime
from app.heatermeter import Heatermeter
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
	# might not need this line
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
	#hm = Heatermeter(True, app.config['SERVER_ADDRESS'], app.config['SERVER_PORT'], app.config['API_KEY'])

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app

from app import models