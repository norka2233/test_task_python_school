from datetime import datetime

from app import db


class Driver(db.Model):
    __tablename__ = 'Driver'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(64), index=True, unique=False)
    lastname = db.Column(db.String(64), index=True, unique=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"{self.id}_{self.firstname}_{self.lastname}"


class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('Driver.id'))
    make = db.Column(db.String(64))
    model = db.Column(db.String(64))
    plate_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"{self.id}_{self.make}_{self.model} owned by Driver #{self.driver_id}."
