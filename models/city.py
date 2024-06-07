#!/usr/bin/python3
"""Creating class city"""
from datetime import datetime
import uuid


class City:
    """City class"""
    def __init__(self, name):
        """Init method"""
        self.name = name
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated_at = self.__created_at
        self.country = None

    @property
    def country(self):
        """Return country"""
        return self.__country

    @country.setter
    def country(self, value):
        """Set country"""
        self.__country = value
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def id(self):
        """Return id"""
        return self.__id

    @property
    def created_at(self):
        """Return created_at"""
        return self.__created_at

    @property
    def updated_at(self):
        """Return updated_at"""
        return self.__updated_at

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
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    def __str__(self):
        """Return string"""
        return self.name

    def __repr__(self):
        """Return string"""
        return self.__str__
