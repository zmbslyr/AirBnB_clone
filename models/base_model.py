#!/usr/bin/python3
""" This module defines the BaseModel class and its attributes """

from datetime import datetime
from os import path
import json
import uuid


class BaseModel:
    """ This class is the model defining all the common attributes for other\
    classes """

    def __init__(self):
        """ This function initializes a new instance of the BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This function print a special string for instances of the BaseModel\
        class """
        return '[%s] (%s) %s' % ('BaseModel', self.id, self.__dict__)

    def save(self):
        """ This function updates and saves the 'updated_at' attribute for \
        instances of the BaseModel class """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """ This function returns a dictionary representation of a BaseModel\
        instance """
        self.__dict__['updated_at'] = '%s' % (self.updated_at.isoformat())
        self.__dict__['created_at'] = '%s' % (self.created_at.isoformat())
        self.__dict__['__class__'] = "BaseModel"
        return self.__dict__
