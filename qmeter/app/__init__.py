from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import json
import time
from datetime import datetime
from app.heatermeter import Heatermeter
from config import Config

db = SQLAlchemy()
scheduler = APScheduler()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

	# might not need this line
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)
    scheduler.start()

	#hm = Heatermeter(True, app.config['SERVER_ADDRESS'], app.config['SERVER_PORT'], app.config['API_KEY'])



    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.before_first_request
    def load_tasks():
        from app import tasks
    return app
#def cleanDatabase():
#    print("deleting session data ")
#    session.query(GrillSessionData).filter(GrillSessionData.id> 0).delete()
#    print("deleting sessions")
#    session.query(GrillSession).filter(GrillSession.id > 0).delete()
#    session.commit()

#def createDefaultSession():
#    if (session.query(GrillSession).filter(GrillSession.id==0).count()) == 0:
#        print("Creating default session...")
#        grillsession = GrillSession(id=0, \
#                                    name='Default Session', \
#                                    description='Session for recording without a defined session', \
#                                    active=1)
#        session.add(grillsession)
#        session.commit()
#        print("Done")
#    else:
#        print("Default session already exists")
#    return

#def main():
    #cleanDatabase()
    #createDefaultSession()

    #job = scheduler.add_job(saveData,'interval', seconds = 1, id='qms')

    #scheduler.start()
    #while True:
    #    time.sleep(5)

#if __name__ == "__main__":
#    main()

#scheduler.add_job(saveData,'interval', seconds = 1)


from app import models