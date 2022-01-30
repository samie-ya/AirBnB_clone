#!/usr/bin/python3
"""Unittest for the function and attribute in class BaseModel"""
import unittest
from models.base_model import BaseModel
from unittest.mock import patch
from datetime import datetime as date
import uuid
import pep8


today = date.now()
later = date.now()
now = date.now()
id1 = str(uuid.uuid4())


class TestBaseModel(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class BaseModel"""

    def setUp(self):
        self.b = BaseModel()

    def test_conformance(self):
        "This tests to confirm to PEP-8"
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Found style error")

    def test_create_at(self):
        self.b.created_at = today
        self.assertEqual(self.b.created_at, today)

    def test_updated_at(self):
        self.b.updated_at = later
        self.assertEqual(self.b.updated_at, later)

    def test_id(self):
        self.b.id = id1
        self.assertEqual(self.b.id, id1)

    def test_save(self):
        self.b.updated_at = now
        self.assertEqual(self.b.updated_at, now)

    def test_str(self):
        self.b.created_at = today
        self.b.updated_at = later
        self.b.id = id1
        on_screen = "[" + type(self.b).__name__ + "]" + " (" + self.b.id + ") \
" + str(self.b.__dict__)
        self.assertEqual(str(self.b), on_screen)

    def test_to_dict(self):
        self.b.created_at = today
        self.b.updated_at = later
        self.b.id = id1
        dic = self.b.to_dict()
        dis = {'updated_at': self.b.updated_at.isoformat(),
               'created_at': self.b.created_at.isoformat(),
               '__class__': str(type(self.b).__name__),
               'id': self.b.id}
        self.assertEqual(dic, dis)

    def test_arguments(self):
        self.b.created_at = today
        self.b.updated_at = later
        self.b.id = id1
        dic = self.b.to_dict()
        bs = BaseModel(**dic)
        self.assertEqual(bs.id, self.b.id)
        self.assertEqual(bs.created_at, self.b.created_at)
        self.assertEqual(bs.updated_at, self.b.updated_at)

    def tearDown(self):
        self.b = None
