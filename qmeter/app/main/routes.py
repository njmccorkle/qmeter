"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, current_app
#from qmeter import app, db
from app import db
from app.main import bp
from app.main.forms import QMSServiceConfigForm

@bp.route('/')
@bp.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@bp.route('/config')
def config():
    """Renders the contact page."""
    form = QMSServiceConfigForm()
    return render_template(
        'config.html',
        title='Config',
        year=datetime.now().year,
        message='Edit qmeter config',
        form=form
    )

@bp.route('/sessions')
def sessions():
    """Renders the contact page."""
    return render_template(
        'sessions.html',
        title='Sessions',
        year=datetime.now().year,
        message='View/edit sessions'
    )

@bp.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
