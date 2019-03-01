from flask_sqlalchemy import SQLAlchemy
from qmeter.models import metadata

db = SQLAlchemy(metadata=metadata)
