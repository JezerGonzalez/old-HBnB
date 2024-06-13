#!/usr/bin/python3
"""Creating class city"""
from datetime import datetime
import uuid
from persistence.DataManager import DataManager


class City:
    """City class"""
    DataManager = DataManager

    def __init__(self, name, country_code):
        """Init method"""
        self.name = name
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated_at = self.__created_at
        self.__country_code = country_code

    @property
    def country_code(self):
        """Return country"""
        return self.__counytry_code

    @country_code.setter
    def country_code(self, value):
        """Set country"""
        self.__counytry_code = value
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

    @classmethod
    def create(cls, name, country_code):
        """Create a new city"""
        city = cls(name, country_code)
        cls.DataManager.save(city)
        return city

    @classmethod
    def get(cls, city_id):
        """Get a specific city by ID"""
        return cls.DataManager.get(city_id, "City")

    def update(self):
        """Update city data"""
        self.DataManager.update(self)

    def delete(self):
        """Delete city"""
        self.DataManager.delete(self.id, "City")

    @classmethod
    def all(cls):
        """Retrieve all cities"""
        return cls.DataManager.all("City")

    def to_dict(self):
        """Return a dictionary representation of a city"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
            "country_id": self.__counytry_code
        }
