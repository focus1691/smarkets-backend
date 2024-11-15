from . import db

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    markets = db.relationship('Market', backref='event', cascade='all, delete')

class Market(db.Model):
    __tablename__ = 'markets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    contracts = db.relationship('Contract', backref='market', cascade='all, delete')

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('markets.id'), nullable=False)

class Competitor(db.Model):
    __tablename__ = 'competitors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class EventCompetitor(db.Model):
    __tablename__ = 'event_competitors'
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    competitor_id = db.Column(db.Integer, db.ForeignKey('competitors.id'), primary_key=True)
