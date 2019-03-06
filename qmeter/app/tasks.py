from flask import current_app
from app import db, scheduler
from app.models import GrillSession, GrillSessionData

@scheduler.task('interval', id='test1', seconds=1, misfire_grace_time=10)
def test():
    print("test")
    return

@scheduler.task('interval', id='qms', seconds=1, misfire_grace_time=10)
def saveData():
    with scheduler.app.app_context():
        #db = Session(engine)
        
        # get current active session
        #activeSession = db.query(GrillSession, GrillSession.id).filter(GrillSession.active==1).first()
        activeSession = GrillSession.query.filter(GrillSession.active==1).first()
        #if not activeSession is not None:
        if activeSession is None:
            #activeSession = db.query(GrillSession).filter(GrillSession.id==0).first()
            activeSession = GrillSession.query.filter(GrillSession.id==0).first()
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
        db.session.add(data)
        db.session.commit()
        return