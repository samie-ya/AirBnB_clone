#!/usr/bin/python3
"""
script for users
"""

from . import base_model


class User(base_model.BaseModel):
    """
    class that defines a User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for User class"""
        super().__init__(self, *args, **kwargs)
