#!/usr/bin/python3


"""
Python script for Base model of all classes
"""


import uuid
import datetime
from models import storage


class BaseModel():
    """
    Base model for all classes
    """

    def __init__(self, *args, **kwargs):
        """constructor method for each object"""
        if len(kwargs) > 0:
            iso_create = kwargs['created_at']
            iso_update = kwargs['updated_at']
            kwargs.pop('__class__')
            kwargs['created_at'] = datetime.datetime.fromisoformat(iso_create)
            kwargs['updated_at'] = datetime.datetime.fromisoformat(iso_update)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            storage.new(self)

    def __str__(self):
        """Unofficial string representation of object"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, str(self.__dict__))

    def save(self):
        """method to update date and time after modification"""
        self.updated_at = datetime.datetime.today()
        storage.save()

    def to_dict(self):
        instance_dict = (self.__dict__).copy()
        instance_dict['created_at'] = (instance_dict['created_at']).isoformat()
        instance_dict['updated_at'] = (instance_dict['updated_at']).isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return (instance_dict)
