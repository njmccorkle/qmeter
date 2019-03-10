import logging
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from app.heatermeter import Heatermeter
from config import Config
from flask_apscheduler import APScheduler
from datetime import datetime 

config = Config()
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
scheduler = APScheduler()


#hm = Heatermeter(True, config.SERVER_ADDRESS, config.SERVER_PORT, config.API_KEY)

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.NOTSET)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
	# might not need this line
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    scheduler.init_app(app)
    scheduler.start()
    
    #hm = Heatermeter(True, app.config['SERVER_ADDRESS'], app.config['SERVER_PORT'], app.config['API_KEY'])

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app

def test():
    print("test = {}".format(datetime.now()))

from app import models