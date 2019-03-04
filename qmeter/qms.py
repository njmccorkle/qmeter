import json
import time  # only for sleep function
from datetime import datetime
#import pytz
from config import Config
from qmeter.heatermeter import Heatermeter
#from sqlalchemy import create_engine
#from sqlalchemy.orm import Session
from qmeter.models import metadata, GrillSession, GrillSessionData
from apscheduler.schedulers.background import BackgroundScheduler

config = Config()
hm = Heatermeter(True, config.SERVER_ADDRESS, config.SERVER_PORT, config.API_KEY)
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
scheduler = BackgroundScheduler()

#grillsession = GrillSession(session_id=0,session_name='Test Session 1')
#session.add(grillsession)
#session.commit()

#works
#temp = session.query(GrillSession).filter(GrillSession.session_id==1).first()
#for i in temp.session_data:
#    print('{}\t{}\t{}'.format(i.timestamp,i.setpoint, i.temp0))

def saveData():
    db = Session(engine)

    # get current active session
    activeSession = db.query(GrillSession, GrillSession.id).filter(GrillSession.active==1).first()
    
    if not activeSession is not None:
        activeSession = db.query(GrillSession).filter(GrillSession.id==0).first()
        activeSession.active = True
        db.commit()

    print("active session: {}".format(activeSession.id))
    parsed = json.loads(hm.sendRequest(hm.apiCalls.status,-1).text)
    data = GrillSessionData(session_id = activeSession.id, \
                            setpoint = parsed['set'], \
                            fan = parsed['fan']['c'], \
                            temp0 = parsed['temps'][0]['c'], \
                            temp1 = parsed['temps'][1]['c'], \
                            temp2 = parsed['temps'][2]['c'], \
                            temp3 = parsed['temps'][3]['c'])
    db.add(data)
    db.commit()

    return


def cleanDatabase():
    print("deleting session data ")
    session.query(GrillSessionData).filter(GrillSessionData.id> 0).delete()
    print("deleting sessions")
    session.query(GrillSession).filter(GrillSession.id > 0).delete()
    session.commit()

def createDefaultSession():
    if (session.query(GrillSession).filter(GrillSession.id==0).count()) == 0:
        print("Creating default session...")
        grillsession = GrillSession(id=0, \
                                    name='Default Session', \
                                    description='Session for recording without a defined session', \
                                    active=1)
        session.add(grillsession)
        session.commit()
        print("Done")
    else:
        print("Default session already exists")
    return

def main():
    #cleanDatabase()
    createDefaultSession()

    job = scheduler.add_job(saveData,'interval', seconds = 1, id='qms')

    scheduler.start()
    while True:
        time.sleep(5)

if __name__ == "__main__":
    main()


#sessions = session.query(GrillSession).all()

#for i in session.query(GrillSession).all():
#    print (i.session_id, i.session_name)

#status = hm.sendRequest(hm.apiCalls.status, -1)
#parsed = json.loads(status.text)
#print(json.dumps(parsed, indent=4, sort_keys=True))

#config = hm.sendRequest(hm.apiCalls.config, -1)
#parsed = json.loads(config.text)
#print(json.dumps(parsed, indent=4, sort_keys=True))
#print(parsed['ip'])