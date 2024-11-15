from app import db

class EventCompetitor(db.Model):
    __tablename__ = 'event_competitors'
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    competitor_id = db.Column(db.Integer, db.ForeignKey('competitors.id'), primary_key=True)
