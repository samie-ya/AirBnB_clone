#!/usr/bin/python3
"""This will create a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class is Review class that inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor method for places
           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
