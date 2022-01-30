#!/usr/bin/python3
"""This function will craete User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all states
           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
