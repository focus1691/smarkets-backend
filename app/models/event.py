from app import db

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    markets = db.relationship('Market', backref='event', cascade='all, delete')
