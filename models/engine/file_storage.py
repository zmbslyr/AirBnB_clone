#!/usr/bin/python3
""" This module defines the FileStorage class and its attributes """

from os import path
import json


class FileStorage:
    """ This class defines the serialization and deserialization of python
    objects """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ This function returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ This function sets in __objects the obj with key
        <obj class name>.id """
        k = obj.__class__.__name__ + "." + obj.id
        v = obj
        FileStorage.__objects[k] = v

    def save(self):
        """ This function serializes __objects to the JSON file
        (path: __file_path) """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        newd = FileStorage.__objects.copy()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            for k, v in newd.items():
                if isinstance(v, BaseModel):
                    instance = v.to_dict
                    FileStorage.__objects[k] = instance
                if isinstance(v, User):
                    instance = v.to_dict
                    FileStorage.__objects[k] = instance
                if isinstance(v, State):
                    instance = v.to_dict
                    FileStorage.__objects[k] = instance
                if isinstance(v, City):
                    instance = v.to_dict
                    FileStorage.__objects[k] = instance
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ This function recreates a BaseModel from another one by using a
        dictionary representation """
        loader = {}
        oth = {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as rfile:
                loader = json.load(rfile)
                FileStorage.__objects = loader
        for k, v in FileStorage.__objects.items():
            oth = BaseModel(None, **v)
            FileStorage.__objects[k] = oth
