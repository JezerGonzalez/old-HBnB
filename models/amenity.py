#!/usr/bin/python3
"""Creating class amenities"""
import uuid
from datetime import datetime
from persistence.DataManager import DataManager


class Amenity:
    """"Amenity class"""
    def __init__(self, name, id=None):
        """Init method"""
        self.__name = name
        self.__id = uuid.uuid4()
        self.__created_at = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated_at = self.created_at

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
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value:
            raise ValueError("name can't be empty")
        self.__name = value
        self.__updated_at = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @classmethod
    def create(cls, name):
        """Create a new amenity"""
        amenity = cls(name)
        cls.data_manager.save(amenity)
        return amenity

    @classmethod
    def get(cls, amenity_id):
        """Get a specific amenity by ID"""
        return cls.data_manager.get(amenity_id, "Amenity")

    def update(self):
        """Update amenity data"""
        self.data_manager.update(self)

    def delete(self):
        """Delete amenity"""
        self.data_manager.delete(self.id, "Amenity")

    @classmethod
    def all(cls):
        """retrieve all amenities"""
        return cls.data_manager.all("Amenity")
