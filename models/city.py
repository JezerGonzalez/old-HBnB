#!/usr/bin/python3
"""Creating class city"""


class City:
    """City class"""
    def __init__(self, name):
        """Init method"""
        self.name = name

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

    def __str__(self):
        """Return string"""
        return self.name

    def __repr__(self):
        """Return string"""
        return self.__str__
