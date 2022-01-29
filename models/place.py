#!/usr/bin/python3
"""
Module for places
"""


from models import base_model


class Place(base_model.BaseModel):
    """
    class for all places
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """constructor method for places"""
        super().__init__(self, *args, **kwargs)
