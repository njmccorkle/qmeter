from datetime import datetime
from flask import render_template, current_app, flash, redirect, url_for, request
#from qmeter import app, db
from app import db, scheduler
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

@bp.route('/config', methods=['GET','POST'])
def config():
    
    form = QMSServiceConfigForm()
    if form.validate_on_submit():

        # native APScheduler scheduler is an object in flask-apscheduler object
        # to reschedule a job we need to access that APScheduler scheduler directly
        sched = scheduler.scheduler
        print("data = {}".format(form.save_interval.data))
        sched.reschedule_job('test', trigger='interval', seconds=form.save_interval.data)

        flash ('QMS save interval set to {} seconds'.format(form.save_interval.data))
        return redirect(url_for('main.config'))

    job = scheduler.get_job('test')
    print(job.trigger.interval)
    w, d = divmod(job.trigger.interval.days, 7)
    mm, ss = divmod(job.trigger.interval.seconds, 60)
    hh, mm = divmod (mm, 60)
    seconds = ss + (mm * 60) + (hh * 60 * 60) + (d * 24 * 60 * 60) + (w * 7 * 24 * 60 * 60)
                
    print("seconds = {}".format(seconds))

    form.save_interval.data = seconds
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
