#!/usr/bin/python3
"""This will create a Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class is Amenity class that inherits from Basemodel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all states
           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
