import json
import time  # only for sleep function
from datetime import datetime
import pytz
from config import Config
from qmeter.heatermeter import Heatermeter
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from qmeter.models import metadata, GrillSession, GrillSessionData

config = Config()
hm = Heatermeter(True, config.SERVER_ADDRESS, config.SERVER_PORT, config.API_KEY)
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)

#grillsession = GrillSession(session_name = 'Test Session 1')
#session.add(grillsession)
#grillsession = GrillSession(session_name = 'Test Session 2')
#session.add(grillsession)
#grillsession = GrillSession(session_name = 'Test Session 3')
#session.add(grillsession)
#session.commit()
data = GrillSessionData(session_id=1,setpoint=200,temp0=100)
session.add(data)
time.sleep(1)
data = GrillSessionData(session_id=1,setpoint=200,temp0=101)
session.add(data)
time.sleep(1)
data = GrillSessionData(session_id=1,setpoint=200,temp0=99)
session.add(data)
time.sleep(1)
data = GrillSessionData(session_id=1,setpoint=200,temp0=102)
session.add(data)
time.sleep(1)
data = GrillSessionData(session_id=1,setpoint=200,temp0=198)
session.add(data)
session.commit()

temp = session.query(GrillSession).filter(GrillSession.session_id==1)
print(temp.session_data)


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
