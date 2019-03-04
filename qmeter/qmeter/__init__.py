"""
The flask application package.
"""
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from qmeter import views, models

import json
import time
from datetime import datetime

#from config import Config
from qmeter.heatermeter import Heatermeter


hm = Heatermeter(True, app.config['SERVER_ADDRESS'], app.config['SERVER_PORT'], app.config['API_KEY'])

db.app = app
db.init_app(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.run()

def test():
    print("test")
    return


#def saveData():
#    #db = Session(engine)

#    # get current active session
#    activeSession = db.query(GrillSession, GrillSession.id).filter(GrillSession.active==1).first()
    
#    if not activeSession is not None:
#        activeSession = db.query(GrillSession).filter(GrillSession.id==0).first()
#        activeSession.active = True
#        db.commit()

#    print("active session: {}".format(activeSession.id))
#    parsed = json.loads(hm.sendRequest(hm.apiCalls.status,-1).text)
#    data = GrillSessionData(session_id = activeSession.id, \
#                            setpoint = parsed['set'], \
#                            fan = parsed['fan']['c'], \
#                            temp0 = parsed['temps'][0]['c'], \
#                            temp1 = parsed['temps'][1]['c'], \
#                            temp2 = parsed['temps'][2]['c'], \
#                            temp3 = parsed['temps'][3]['c'])
#    db.add(data)
#    db.commit()

#    return

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