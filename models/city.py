#!/usr/bin/python3
"""This will create a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class is City class that inherits from Basemodel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all cities
           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
