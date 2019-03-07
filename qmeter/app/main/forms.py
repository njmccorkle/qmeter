from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QMSServiceConfigForm (FlaskForm):
    service_interval = IntegerField('qms Save Interval')
    submit = SubmitField('Set Interval')