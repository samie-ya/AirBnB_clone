#!/usr/bin/python3
"""Unittest for the function and attribute in class Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User
from unittest.mock import patch
from datetime import datetime as date
import uuid


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())
id2 = str(uuid.uuid4())
id3 = str(uuid.uuid4())


class TestReview(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class Review"""

    def setUp(self):
        self.r = Review()
        self.p = Place()
        self.p.id = id2
        self.u = User()
        self.u.id = id3

    def test_create_at(self):
        self.r.created_at = today
        self.assertEqual(self.r.created_at, today)

    def test_updated_at(self):
        self.r.updated_at = later
        self.assertEqual(self.r.updated_at, later)

    def test_id(self):
        self.r.id = id1
        self.assertEqual(self.r.id, id1)

    def test_save(self):
        self.r.updated_at = now
        self.assertEqual(self.r.updated_at, now)

    def test_str(self):
        self.r.created_at = today
        self.r.updated_at = later
        self.r.id = id1
        self.r.place_id = self.p.id
        self.r.user_id = self.u.id
        on_screen = "[" + type(self.r).__name__ + "]" + " (" + self.r.id + ") \
" + str(self.r.__dict__)
        self.assertEqual(str(self.r), on_screen)

    def test_to_dict(self):
        self.r.created_at = today
        self.r.updated_at = later
        self.r.id = id1
        self.r.place_id = self.p.id
        self.r.user_id = self.u.id
        dic = self.r.to_dict()
        dis = {'updated_at': self.r.updated_at.isoformat(),
               'created_at': self.r.created_at.isoformat(),
               '__class__': str(type(self.r).__name__),
               'id': self.r.id,
               'place_id': self.r.place_id,
               'user_id': self.r.user_id}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.p = None
        self.u = None
        self.r = None
