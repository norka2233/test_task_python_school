from datetime import datetime
import unittest
from app import app, db
from app.models import Driver, Vehicle


class Driver_Test(unittest.TestCase):
    def set_up(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()

    def test_driver_create(self):
        d_1 = Driver(firstname='pesyk', lastname='mesyk',)
        d_2 = Driver(firstname='kytsyk', lastname='mytsyk',)
        db.session.add(d_1)
        db.session.add(d_2)
        db.session.commit()
        self.assertEqual(d_1.firstname, 'pesyk')
        self.assertEqual(d_1.lastname, 'mesyk')

    def test_driver_edit(self):
        d_1 = Driver(firstname='rap', lastname='mesyk',)
        db.session.add(d_1)
        db.session.commit()
        self.assertEqual(d_1.firstname, 'rap')


class Vehicle_Test():
    def set_up(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()

    def test_vehicle_create(self):
        v_1 = Vehicle(make='nissan', model='x-trail', driver_id=1)
        db.session.add(v_1)
        db.session.commit()
        self.assertEqual(v_1.make, 'nissan')
        self.assertEqual(v_1.driver_id, 1)

    def test_vehicle_edit(self):
        v_1 = Vehicle(make='dodge', model='charger', driver_id=8)
        db.session.add(v_1)
        db.session.commit()
        self.assertEqual(v_1.make, 'dodge')
        self.assertEqual(v_1.driver_id, 8)