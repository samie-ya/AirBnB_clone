#!/usr/bin/python3
"""This will create a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class is Review class that inherits from Basemodel"""
    place_id = ""
    used_id = ""
    text = ""
