#!/usr/bin/python3
""" This module defines the BaseModel class and its attributes """

from datetime import datetime
import uuid


class BaseModel:
    """ This class is the model defining all the common attributes for other
    classes """

    def __init__(self, *args, **kwargs):
        """ This function initializes a new instance of the BaseModel class """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k == 'updated_at':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k == '__class__':
                    v = self.__class__
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ This function print a special string for instances of the BaseModel
        class """
        return '[%s] (%s) %s' % (self.__class__.__name__, self.id,
                                 self.__dict__)

    def save(self):
        """ This function updates and saves the 'updated_at' attribute for
        instances of the BaseModel class """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ This function returns a dictionary representation of a BaseModel
        instance """
        if type(self.updated_at) is str:
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
        if type(self.created_at) is str:
            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
        dcpy = self.__dict__.copy()
        dcpy['updated_at'] = '%s' % (self.updated_at.isoformat())
        dcpy['created_at'] = '%s' % (self.created_at.isoformat())
        dcpy['__class__'] = self.__class__.__name__
        return dcpy
