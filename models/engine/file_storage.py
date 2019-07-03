#!/usr/bin/python3
""" This module defines the FileStorage class and its attributes """

from models.base_model import BaseModel
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
        for k, v in FileStorage.__objects.items():
            if type(v) is not dict:
                FileStorage.__objects[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ This function recreates a BaseModel from another one by using a
        dictionary representation """
        oth = {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as rfile:
                loader = json.load(rfile)
                FileStorage.__objects = loader
        for k, v in FileStorage.__objects.items():
            oth = BaseModel(None, **v)
            FileStorage.__objects[k] = oth
