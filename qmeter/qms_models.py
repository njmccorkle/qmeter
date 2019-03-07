from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class GrillSession(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    description = Column(String(500))
    session_data = relationship('GrillSessionData', back_populates='grillsession')
    type = Column(Integer)
    active = Column(Boolean)


class GrillSessionData(Base):
    __tablename__ = 'session_data'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    grillsession = relationship("GrillSession", back_populates='session_data')
    setpoint = Column(Integer)
    fan = Column(Integer)
    temp0 = Column(Numeric(precision=2))
    temp1 = Column(Numeric(precision=2))
    temp2 = Column(Numeric(precision=2))
    temp3 = Column(Numeric(precision=2))
    timestamp = Column(DateTime, default=datetime.utcnow)