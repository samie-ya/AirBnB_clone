#!/usr/bin/python3
"""Unittest for the function and attribute in class BaseModel"""
import unittest
from models.base_model import BaseModel
from unittest.mock import patch
import datetime
count = 0
def mock_uid():
    global count
    count += 1
    return uuid.uuid()

class TestBaseModel(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class BaseModel"""
    def setUp(self, **kwargs):
        self.base  = BaseModel()
        self.__create_obj

    def test_create_at(self):
        with patch('datetime.datetime') as dt:
            dt.now.return_value = '2022-01-28 19:09:33.962098'
            res = self.base.created_at
            self.assertEqual(self.base.created_at, res)

    def test_update_at(self):
        with patch('datetime.datetime') as dt:
            dt.now.return_value = '2022-01-28 19:09:33.962345'
            res = self.base.updated_at
            self.assertEqual(self.base.updated_at, res)

    @patch('uuid.uuid4', mock_uid)
    def __create_obj(self):
        self.assertEqual(self.base.id, "abe7c0b1-da34-4fa4-ad10-0b444030b77c")
        
