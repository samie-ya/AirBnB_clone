#!/usr/bin/python3
"""This will create a State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class is State class that inherits from Basemodel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all states
           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
