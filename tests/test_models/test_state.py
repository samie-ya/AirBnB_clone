#!/usr/bin/python3
"""Unittest for the function and attribute in class State"""
import unittest
from models.base_model import BaseModel
from models.state import State
from unittest.mock import patch
from datetime import datetime as date
import uuid
import pycodestyle


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())


class TestState(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class State"""

    def setUp(self):
        self.s = State()

    def test_conformance(self):
        "This tests to confirm to PEP-8"
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(['models/state.py'])
        self.assertEqual(res.total_errors, 0, "Found style error")

    def test_create_at(self):
        self.s.created_at = today
        self.assertEqual(self.s.created_at, today)

    def test_updated_at(self):
        self.s.updated_at = later
        self.assertEqual(self.s.updated_at, later)

    def test_id(self):
        self.s.id = id1
        self.assertEqual(self.s.id, id1)

    def test_save(self):
        self.s.updated_at = now
        self.assertEqual(self.s.updated_at, now)

    def test_str(self):
        self.s.created_at = today
        self.s.updated_at = later
        self.s.id = id1
        self.s.name = "California"
        on_screen = "[" + type(self.s).__name__ + "]" + " (" + self.s.id + ") \
" + str(self.s.__dict__)
        self.assertEqual(str(self.s), on_screen)

    def test_to_dict(self):
        self.s.created_at = today
        self.s.updated_at = later
        self.s.id = id1
        self.s.name = "California"
        dic = self.s.to_dict()
        dis = {'updated_at': self.s.updated_at.isoformat(),
               'created_at': self.s.created_at.isoformat(),
               '__class__': str(type(self.s).__name__),
               'id': self.s.id,
               'name': self.s.name}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.s = None
