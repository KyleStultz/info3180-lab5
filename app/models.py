# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime
import pytz

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    string = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now()
        #self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")