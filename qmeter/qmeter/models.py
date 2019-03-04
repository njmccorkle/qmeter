from datetime import datetime
from qmeter import db

class GrillSession(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    session_data = db.relationship('GrillSessionData', back_populates='grillsession')
    type = db.Column(db.Integer)
    active = db.Column(db.Boolean)


class GrillSessionData(db.Model):
    __tablename__ = 'session_data'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    grillsession = db.relationship("GrillSession", back_populates='session_data')
    setpoint = db.Column(db.Integer)
    fan = db.Column(db.Integer)
    temp0 = db.Column(db.Numeric(precision=2))
    temp1 = db.Column(db.Numeric(precision=2))
    temp2 = db.Column(db.Numeric(precision=2))
    temp3 = db.Column(db.Numeric(precision=2))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)