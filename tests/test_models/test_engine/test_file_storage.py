#!/usr/bin/python3
"""
Test module for file storage
"""

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
        """creating instance of FileStorage"""
        self.storage = FileStorage()
        self.basemodel = BaseModel()
        self.user = User()
        self.amenity = Amenity()
        self.city = City()
        self.state = State()
        self.place = Place()
        self.review = Review()

    def test_all(self):
        file_path = 'file.json'
        with open(file_path, "w", encoding='utf-8') as f:
            f.write('')
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
        self.new_user = User()
        current_objects = self.storage.all()
        new_key = 'User.' + self.new_user.id
        self.assertEqual(current_objects[new_key], self.new_user)
