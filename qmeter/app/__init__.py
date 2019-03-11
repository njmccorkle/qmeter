import logging
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from app.heatermeter import Heatermeter
from config import Config
from flask_apscheduler import APScheduler
from datetime import datetime
from app.models import GrillSession, GrillSessionData

config = Config()
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
scheduler = APScheduler()

hm = Heatermeter(True, config.SERVER_ADDRESS, config.SERVER_PORT, config.API_KEY)

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
    job = scheduler.get_job('qms')

    if job == None:
        print("No qms job found. Creating new job.")
        sched = scheduler.scheduler
        sched.add_job(saveData, 'interval', seconds=2, id='qms', coalesce=True)
    else:
        print("Found qms job. Not creating new job")
    
    #hm = Heatermeter(True, app.config['SERVER_ADDRESS'], app.config['SERVER_PORT'], app.config['API_KEY'])

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app

def test():
    print("test = {}".format(datetime.now()))
    return

def saveData():
    # need to move this to another spot.
    # saveData requires GrillSession. GrillSession requires app. Circular
    print("saving data {}".format(datetime.now()))
    with db.app.app_context():
        #db = Session(engine)

        # get current active session
        #activeSession = db.query(GrillSession, GrillSession.id).filter(GrillSession.active==1).first()
        activeSession = GrillSession.query.filter(activeSession==1).first()
    
        if not activeSession is not None:
            activeSession = GrillSession.query.filter(id==0).first()
            #activeSession = db.query(GrillSession).filter(GrillSession.id==0).first()
            activeSession.active = True
            #db.commit()
            session.commit()

        print("active session: {}".format(activeSession.id))
        parsed = json.loads(hm.sendRequest(hm.apiCalls.status,-1).text)
        data = GrillSessionData(session_id = activeSession.id, \
                                setpoint = parsed['set'], \
                                fan = parsed['fan']['c'], \
                                temp0 = parsed['temps'][0]['c'], \
                                temp1 = parsed['temps'][1]['c'], \
                                temp2 = parsed['temps'][2]['c'], \
                                temp3 = parsed['temps'][3]['c'])
        #db.add(data)
        #db.commit()
        session.add(data)
        session.commit()

        return

#def saveData():
#    #print("saveData {}".format(datetime.now()))
#    #return
#    with db.app.app_context():
#        db = Session(engine)

#        # get current active session
#        activeSession = db.query(GrillSession, GrillSession.id).filter(GrillSession.active==1).first()
    
#        if not activeSession is not None:
#            activeSession = db.query(GrillSession).filter(GrillSession.id==0).first()
#            activeSession.active = True
#            db.commit()

#        print("active session: {}".format(activeSession.id))
#        parsed = json.loads(hm.sendRequest(hm.apiCalls.status,-1).text)
#        data = GrillSessionData(session_id = activeSession.id, \
#                                setpoint = parsed['set'], \
#                                fan = parsed['fan']['c'], \
#                                temp0 = parsed['temps'][0]['c'], \
#                                temp1 = parsed['temps'][1]['c'], \
#                                temp2 = parsed['temps'][2]['c'], \
#                                temp3 = parsed['temps'][3]['c'])
#        db.add(data)
#        db.commit()

#        return

from app import models
