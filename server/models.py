
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bakery(db.Model):
    __tablename__ = 'bakeries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class BakedGood(db.Model):
    __tablename__ = 'baked_goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    bakery = db.relationship('Bakery', backref='baked_goods')
    