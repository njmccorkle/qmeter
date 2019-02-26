from datetime import datetime
#from app import db

class Session(object):
    __tablename__ = 'sessions'
    session_id = db.Column(db.Integer, primary_key=True)
    session_name = db.Column(db.String(120), Index=True)
    sessions = db.relationship('SessionData',backref='session', lazy='dynamic')

class SessionData(object):
    __tablename__ = 'session_data'
    session_id = db.Column(db.Integer, db.ForeignKey('session.session_id'))
    setpoint = db.Column(db.Integer)
    fan = db.Column(db.Integer)
    temp0 = db.Column(db.Integer)
    temp1 = db.Column(db.Integer)
    temp2 = db.Column(db.Integer)
    temp3 = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)