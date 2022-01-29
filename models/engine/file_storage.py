#!/usr/bin/python3
"""This will create a File Storage to serialize and deserialize"""
import json
import os


class FileStorage:
    """This is the class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This function returns the dictionary in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This function sets the obj with id and class name

           Args:
                obj (object): this is the object of the class
        """
        class_name = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[class_name] = obj

    def save(self):
        """This function serializes __objects to a json file"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            dic = {}
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
            f.write(json.dumps(dic))

    def reload(self):
        """This function deserializes the contents of json file
           into __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                dic = {}
                dic.update(json.loads(f.read()))
                for key, value in dic.items():
                    for k, v in value.items():
                        for a, b in classes.items():
                            if v == a:
                                FileStorage.__objects[key] = b(**value)
