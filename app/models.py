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


# class Vehicle(db.Model):
#     id = uuid.uuid4()
#     driver_id = "driver_id"
#     make = "VW"
#     model = "Golf mk7"
#     plate_number = "AA 1234 OO"
#     created_at = "car_created at"
#     updated_at = "car_updated_at"
