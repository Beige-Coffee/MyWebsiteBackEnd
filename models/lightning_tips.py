from db import db
import datetime

class LightningTipsModel(db.Model):
    __tablename__ = 'LIGHTNING_TIPS'

    id = db.Column(db.Integer, primary_key=True)
    payment_hash = db.Column(db.String(100), unique=True, nullable=False)
    payment_request = db.Column(db.String(1000), unique=True, nullable=False)
    status = db.Column(db.String(100), unique=False, nullable=False, default="Invoice generated.")
    generatated_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.datetime.utcnow)
    paid_at = db.Column(db.DateTime, unique=False, nullable=True)
    memo = db.Column(db.String(1000), unique=False, nullable=True)
    amount = db.Column(db.Integer, unique=False, nullable=False)