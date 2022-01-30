#!/usr/bin/python3
"""This function will craete User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
