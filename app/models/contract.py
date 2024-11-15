from app import db

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('markets.id'), nullable=False)