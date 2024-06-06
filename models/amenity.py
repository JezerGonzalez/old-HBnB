#!/usr/bin/python3
"""Creating class amenities"""
import uuid
import datetime


class Amenity:
    """"Amenity class"""
    def __init__(self, name, id=None):
        """Init method"""
        self.name = name
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    @property
    def id(self):
        """Return id"""
        return self.__id

    @property
    def name(self):
        """Return name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set name"""
        self.__name = value
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value:
            raise ValueError("name can't be empty")
        if not value.isalpha():
            raise ValueError("name must contain only letters")
