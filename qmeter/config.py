import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_KEY="5c4dfbd597b59c9af5a218a0dff00b9a"
    SERVER_ADDRESS="heatermeter.mccorkle.co"
    SERVER_PORT=80

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'qmeter.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # define APScheduler job for qmeter data service
    JOBS = [
        {
            'id': 'qms',
            'func': 'test',
            'trigger': 'interval',
            'seconds': 2
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }

    SCHEDULER_API_ENABLED = True

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir,'app.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['njmccorkle@gmail.com']

    POSTS_PER_PAGE = 10
    LANGUAGES = ['en','es']
