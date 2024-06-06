#!/usr/python3
"""User class for the HBnB Evolution project"""
import uuid, datetime
from .places import Places


class User:
    """Class defining any HBnB users"""

    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__created = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated = self. created
        self.__id = str(uuid.uuid4())
        self.__places = []

    def add_place(self, place):
        """Adds a place to the list of places"""
        if not isinstance(place, Places):
            raise TypeError("place must be an instance of Place")
        self.__places.append(place)
        place.host_id = self.__id
        place.host_name = self.__first_name + " " + self.__last_name
        place.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @property
    def created(self):
        """Getter for created"""
        return self.__created

    @property
    def updated(self):
        """Getter for updated"""
        return self.__updated

    @property
    def first_name(self):
        """Getter for first name"""
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets first name"""
        if type(first_name) is not str:
            raise TypeError("Name must be a string")
        if len(first_name) == 0:
            raise ValueError("Name must not be empty")
        self.__first_name = first_name
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
    @property
    def last_name(self):
        """Getter for last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """Last name setter"""
        if type(last_name) is not str:
            raise TypeError("Last name must be a string")
        if len(last_name) == 0:
            raise ValueError("Last name must not be empty")
        self.__last_name = last_name
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
    @property
    def email(self):
        """Email Getter"""
        return self.__email

    @email.setter
    def email(self, email):
        """Email setter"""
        if type(email) is not str:
            raise TypeError("Email must be a string")
        if len(email) == 0:
            raise ValueError("Email must not be empty")
        self.__email = email
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, password):
        """Password setter"""
        if type(password) is not str:
            raise TypeError("Password must be a string")
        if len(password) == 0:
            raise ValueError("Password must not be empty")
        self.__password = password
        self.updated = datetime.datetime.now().strftime("%b/%d/%y %I:%M %p")
