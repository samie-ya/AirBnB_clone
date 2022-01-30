#!/usr/bin/python3
"""
Test module for file storage
"""

import pycodestyle
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test class for the methods of the file storage class
    """

    def setUp(self):
        """setup method for testing"""
        self.storage = FileStorage()
        self.basemodel = BaseModel()
        self.user = User()
        self.amenity = Amenity()
        self.city = City()
        self.state = State()
        self.place = Place()
        self.review = Review()

    def test_conformance(self):
        "This tests to confirm to PEP-8"
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0, "Found style error")

    def test_all(self):
        """This tests the function all in file_storage"""
        all_objects = self.storage.all()
        base_key = 'BaseModel.' + self.basemodel.id
        self.assertEqual(all_objects[base_key], self.basemodel)
        user_key = 'User.' + self.user.id
        self.assertEqual(all_objects[user_key], self.user)
        amen_key = 'Amenity.' + self.amenity.id
        self.assertEqual(all_objects[amen_key], self.amenity)
        city_key = 'City.' + self.city.id
        self.assertEqual(all_objects[city_key], self.city)
        state_key = 'State.' + self.state.id
        self.assertEqual(all_objects[state_key], self.state)
        place_key = 'Place.' + self.place.id
        self.assertEqual(all_objects[place_key], self.place)
        rev_key = 'Review.' + self.review.id
        self.assertEqual(all_objects[rev_key], self.review)

    def test_save(self):
        """This function will test the save function of file_storage"""
        file_path = 'file.json'
        with open(file_path, "w", encoding='utf-8') as f:
            f.write('')
        self.storage.save()
        with open(file_path, "r", encoding='utf-8') as f:
            file_contents = f.read()
        all_objects = json.loads(file_contents)
        base_key = 'BaseModel.' + self.basemodel.id
        self.assertEqual(all_objects[base_key], self.basemodel.to_dict())
        user_key = 'User.' + self.user.id
        self.assertEqual(all_objects[user_key], self.user.to_dict())
        amen_key = 'Amenity.' + self.amenity.id
        self.assertEqual(all_objects[amen_key], self.amenity.to_dict())
        city_key = 'City.' + self.city.id
        self.assertEqual(all_objects[city_key], self.city.to_dict())
        state_key = 'State.' + self.state.id
        self.assertEqual(all_objects[state_key], self.state.to_dict())
        place_key = 'Place.' + self.place.id
        self.assertEqual(all_objects[place_key], self.place.to_dict())
        rev_key = 'Review.' + self.review.id
        self.assertEqual(all_objects[rev_key], self.review.to_dict())

    def test_new(self):
        """This function will test the new function of storage"""
        self.user = User()
        current_objects = self.storage.all()
        new_key = 'User.' + self.user.id
        self.assertEqual(current_objects[new_key], self.user)
        self.basemodel = BaseModel()
        new_key = 'BaseModel.' + self.basemodel.id
        self.assertEqual(current_objects[new_key], self.basemodel)
        self.amenity = Amenity()
        new_key = 'Amenity.' + self.amenity.id
        self.assertEqual(current_objects[new_key], self.amenity)
        self.city = City()
        new_key = 'City.' + self.city.id
        self.assertEqual(current_objects[new_key], self.city)
        self.state = State()
        new_key = 'State.' + self.state.id
        self.assertEqual(current_objects[new_key], self.state)
        self.place = Place()
        new_key = 'Place.' + self.place.id
        self.assertEqual(current_objects[new_key], self.place)
        self.review = Review()
        new_key = 'Review.' + self.review.id
        self.assertEqual(current_objects[new_key], self.review)

    def tearDown(self):
        """Tears down the attributes set in setup"""
        self.storage = None
        self.basemodel = None
        self.user = None
        self.amenity = None
        self.city = None
        self.state = None
        self.place = None
        self.review = None


if __name__ == '__main__':
    unittest.main()
