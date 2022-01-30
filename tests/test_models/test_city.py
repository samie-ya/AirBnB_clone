#!/usr/bin/python3
"""Unittest for the function and attribute in class City"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from unittest.mock import patch
from datetime import datetime as date
import uuid
import pycodestyle


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())
id2 = str(uuid.uuid4())


class TestCity(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class City"""

    def setUp(self):
        self.c = City()
        self.s = State()
        self.s.id = id2

    def test_conformance(self):
        "This tests to confirm to PEP-8"
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "Found style error")

    def test_create_at(self):
        self.c.created_at = today
        self.assertEqual(self.c.created_at, today)

    def test_updated_at(self):
        self.c.updated_at = later
        self.assertEqual(self.c.updated_at, later)

    def test_id(self):
        self.c.id = id1
        self.assertEqual(self.c.id, id1)

    def test_save(self):
        self.c.updated_at = now
        self.assertEqual(self.c.updated_at, now)

    def test_str(self):
        self.c.created_at = today
        self.c.updated_at = later
        self.c.id = id1
        self.c.state_id = self.s.id
        self.c.name = "LA"
        on_screen = "[" + type(self.c).__name__ + "]" + " (" + self.c.id + ") \
" + str(self.c.__dict__)
        self.assertEqual(str(self.c), on_screen)

    def test_to_dict(self):
        self.c.created_at = today
        self.c.updated_at = later
        self.c.id = id1
        self.c.state_id = self.s.id
        self.c.name = "LA"
        dic = self.c.to_dict()
        dis = {'updated_at': self.c.updated_at.isoformat(),
               'created_at': self.c.created_at.isoformat(),
               '__class__': str(type(self.c).__name__),
               'id': self.c.id,
               'state_id': self.c.state_id,
               'name': self.c.name}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.s = None
        self.c = None
