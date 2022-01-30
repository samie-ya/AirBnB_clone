#!/usr/bin/python3
"""This will create a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class is City class that inherits from Basemodel"""
    state_id = ""
    name = ""
