#!/usr/bin/python3
"""Unittest for the function and attribute in class User"""
import unittest
from models.base_model import BaseModel
from models.user import User
from unittest.mock import patch
from datetime import datetime as date
import uuid


today = date(year=2022, month=1, day=30)
later = date(year=2022, month=1, day=30)
now = date.now()
id1 = str(uuid.uuid4())


class TestUser(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class User"""

    def setUp(self):
        self.u = User()

    def test_create_at(self):
        self.u.created_at = today
        self.assertEqual(self.u.created_at, today)

    def test_updated_at(self):
        self.u.updated_at = later
        self.assertEqual(self.u.updated_at, later)

    def test_id(self):
        self.u.id = id1
        self.assertEqual(self.u.id, id1)

    def test_save(self):
        self.u.updated_at = now
        self.assertEqual(self.u.updated_at, now)

    def test_str(self):
        self.u.created_at = today
        self.u.updated_at = later
        self.u.email = "samrasolomon@40gmail.com"
        self.u.password = "1234"
        self.u.first_name = "Samra"
        self.u.last_name = "Solomon"
        self.u.id = id1
        on_screen = "[" + type(self.u).__name__ + "]" + " (" + self.u.id + ") \
" + str(self.u.__dict__)
        self.assertEqual(str(self.u), on_screen)

    def test_to_dict(self):
        self.u.created_at = today
        self.u.updated_at = later
        self.u.id = id1
        self.u.email = "samrasolomon@40gmail.com"
        self.u.password = "1234"
        self.u.first_name = "Samra"
        self.u.last_name = "Solomon"
        dic = self.u.to_dict()
        dis = {'updated_at': self.u.updated_at.isoformat(),
               'created_at': self.u.created_at.isoformat(),
               '__class__': str(type(self.u).__name__),
               'id': self.u.id,
               'email': self.u.email,
               'password': self.u.password,
               'first_name': self.u.first_name,
               'last_name': self.u.last_name}
        self.assertEqual(dic, dis)

    def tearDown(self):
        self.u = None
