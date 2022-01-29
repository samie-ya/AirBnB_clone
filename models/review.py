#!/usr/bin/python3
"""
reviews module
"""

from models import base_model


class Review(base_model.BaseModel):
    """
    class for all reviews
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all cities"""
        super().__init__(self, *args, **kwargs)
