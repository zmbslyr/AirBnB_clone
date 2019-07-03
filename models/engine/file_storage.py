#!/usr/bin/python3
""" This module defines the FileStorage class and its attributes """

from os import path
import json


class FileStorage:
    """ This class defines the serialization and deserialization of python\
    objects """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ This function returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ This function sets in __objects the obj with key \
        <obj class name>.id """
        k = obj.__class__.__name__ + "." + obj.id
        v = obj
        FileStorage.__objects[k] = v

    def save(self):
        """ This function serializes __objects to the JSON file \
        (path: __file_path) """
        from models.base_model import BaseModel
        for k, v in FileStorage.__objects.items():
            if type(v) is not dict:
                FileStorage.__objects[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        from models.base_model import BaseModel
        loader = {}
        oth = {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as rfile:
                loader = json.load(rfile)
                for k, v in loader.items():
                    oth = v
                    if oth["__class__"] == "BaseModel":
                        instance = BaseModel(**oth)
                    if oth["__class__"] == "User":
                        instance = User(**oth)
                    loader[k] = instance
                FileStorage.__objects = loader
