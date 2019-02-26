import json
from datetime import datetime
import pytz
from config import Config
from heatermeter import Heatermeter
from models import Session, SessionData
#from flask_sqlalchemy import SQLAlchemy
import SQLAlchemy
import alembic
#from flask_migrate import Migrate


config = Config()
hm = Heatermeter(True, config.SERVER_ADDRESS, config.SERVER_PORT, config.API_KEY)
db = SQLAlchemy()
migrate = Migrate (db)

#data = hm.sendRequest(hm.apiCalls.tempsXn, 0)
#print(data.text)
status = hm.sendRequest(hm.apiCalls.status, -1)
parsed = json.loads(status.text)
print(json.dumps(parsed, indent=4, sort_keys=True))

config = hm.sendRequest(hm.apiCalls.config, -1)
parsed = json.loads(config.text)
print(json.dumps(parsed, indent=4, sort_keys=True))
print(parsed['ip'])
#data = hm.sendRequest(hm.apiCalls.fan, -1)
#print(data.text)


#r = requests.get(url, params=requestParams)
##print(r.status_code)
##print(r.encoding)
##print(r.headers)
##print(r.text)
##print(r.json())

#d = json.loads(r.text)

#print (d['time'])
#print(datetime.utcfromtimestamp(d['time']).strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.now())
##print(pytz.utc.localize(datetime.utcfromtimestamp(d['time']).strftime('%Y-%m-%d %H:%M:%S')))