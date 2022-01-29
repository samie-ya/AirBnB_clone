#!/usr/bin/python3
"""
amenities module
"""

from models import base_model


class Amenity(base_model.BaseModel):
    """
    class for all Amenities
    """
    
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all amenities"""
        super().__init__(self, *args, **kwargs)
