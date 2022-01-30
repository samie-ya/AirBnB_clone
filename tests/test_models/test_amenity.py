#!/usr/bin/python3
"""Unittest for the function and attribute in class Amenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from unittest.mock import patch
from datetime import datetime as date
import uuid
import pycodestyle


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())


class TestAmenity(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class Amenity"""

    def setUp(self):
        self.a = Amenity()

    def test_conformance(self):
        "This tests to confirm to PEP-8"
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Found style error")

    def test_create_at(self):
        self.a.created_at = today
        self.assertEqual(self.a.created_at, today)

    def test_updated_at(self):
        self.a.updated_at = later
        self.assertEqual(self.a.updated_at, later)

    def test_id(self):
        self.a.id = id1
        self.assertEqual(self.a.id, id1)

    def test_save(self):
        self.a.updated_at = now
        self.assertEqual(self.a.updated_at, now)

    def test_str(self):
        self.a.created_at = today
        self.a.updated_at = later
        self.a.id = id1
        on_screen = "[" + type(self.a).__name__ + "]" + " (" + self.a.id + ") \
" + str(self.a.__dict__)
        self.assertEqual(str(self.a), on_screen)

    def test_to_dict(self):
        self.a.created_at = today
        self.a.updated_at = later
        self.a.id = id1
        self.a.name = "Motel"
        dic = self.a.to_dict()
        dis = {'updated_at': self.a.updated_at.isoformat(),
               'created_at': self.a.created_at.isoformat(),
               '__class__': str(type(self.a).__name__),
               'id': self.a.id,
               'name': self.a.name}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.a = None
