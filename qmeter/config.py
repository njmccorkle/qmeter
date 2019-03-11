import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import app

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_KEY="5c4dfbd597b59c9af5a218a0dff00b9a"
    SERVER_ADDRESS="heatermeter.mccorkle.co"
    SERVER_PORT=80
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'qmeter.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # use this for flask-APSCheduler NOT APScheduler
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }

    #this works but can't do it here. new job every time a page is loaded
    #JOBS = [
    #    {
    #        'id': 'qms',
    #        'func': 'app:saveData',
    #        'trigger':'interval',
    #        'seconds': 1}]
    
    ## use this for APSCheduler NOT flask-APScheduler
    #SCHEDULER_JOBSTORES = {
    #    'apscheduler.jobstores.default': {
    #    'type': 'sqlalchemy',
    #    'url': SQLALCHEMY_DATABASE_URI}
    #}

    SCHEDULER_API_ENABLED = True

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['njmccorkle@gmail.com']

    POSTS_PER_PAGE = 10
    LANGUAGES = ['en','es']
