#!/usr/bin/python3
"""Unittest for the function and attribute in class Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from unittest.mock import patch
from datetime import datetime as date
import uuid


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())
id2 = str(uuid.uuid4())
id3 = str(uuid.uuid4())
id4 = str(uuid.uuid4())


class TestPlace(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class Place"""

    def setUp(self):
        self.p = Place()
        self.u = User()
        self.a = Amenity()
        self.c = City()
        self.u.id = id2
        self.c.id = id3
        self.a.id = id4

    def test_create_at(self):
        self.p.created_at = today
        self.assertEqual(self.p.created_at, today)

    def test_updated_at(self):
        self.p.updated_at = later
        self.assertEqual(self.p.updated_at, later)

    def test_id(self):
        self.p.id = id1
        self.assertEqual(self.p.id, id1)

    def test_save(self):
        self.p.updated_at = now
        self.assertEqual(self.p.updated_at, now)

    def test_str(self):
        self.p.created_at = today
        self.p.updated_at = later
        self.p.id = id1
        self.p.city_id = self.c.id
        self.p.user_id = self.u.id
        self.p.name = "Stay Rested"
        self.p.description = "It is a motel on Main Street"
        self.p.number_rooms = 20
        self.p.number_bathrooms = 22
        self.p.max_guest = 80
        self.p.price_by_night = 20
        self.p.latitude = 34.0522
        self.p.longtitude = 118.2437
        self.p.amenity_ids = [self.a.id]
        on_screen = "[" + type(self.p).__name__ + "]" + " (" + self.p.id + ") \
" + str(self.p.__dict__)
        self.assertEqual(str(self.p), on_screen)

    def test_to_dict(self):
        self.p.created_at = today
        self.p.updated_at = later
        self.p.id = id1
        self.p.city_id = self.c.id
        self.p.user_id = self.u.id
        self.p.name = "Stay Rested"
        self.p.description = "It is a motel on Main Street"
        dic = self.p.to_dict()
        dis = {'updated_at': self.p.updated_at.isoformat(),
               'created_at': self.p.created_at.isoformat(),
               '__class__': str(type(self.p).__name__),
               'id': self.p.id,
               'city_id': self.p.city_id,
               'user_id': self.p.user_id,
               'name': self.p.name,
               'description': self.p.description}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.p = None
        self.c = None
        self.s = None
        self.a = None
