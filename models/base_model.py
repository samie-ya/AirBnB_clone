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
        """constructor method for each object

           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
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
        """This function will take the value of __dict__ and add a new key
           __class__ and will change the format of created_at and updated_at
           to a string format"""
        instance_dict = (self.__dict__).copy()
        instance_dict['created_at'] = (instance_dict['created_at']).isoformat()
        instance_dict['updated_at'] = (instance_dict['updated_at']).isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return (instance_dict)
