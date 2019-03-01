from datetime import datetime
from sqlalchemy import MetaData, Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class GrillSession(Base):
    __tablename__ = 'sessions'
    session_id = Column(Integer, primary_key=True)
    session_name = Column(String(120))
    #session = relationship('GrillSessionData',back_populates='session', lazy='dynamic')
    session_data = relationship('GrillSessionData', backref='session')

class GrillSessionData(Base):
    __tablename__ = 'session_data'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.session_id'))
    #session = relationship('GrillSession', back_populates='session_data')
    setpoint = Column(Integer)
    fan = Column(Integer)
    temp0 = Column(Integer)
    temp1 = Column(Integer)
    temp2 = Column(Integer)
    temp3 = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)