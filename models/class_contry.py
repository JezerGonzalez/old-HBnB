from .city import City


class Country:
    """Defines a country"""

    def __init__(self, name):
        """Initialize with a name"""
        self.name = name
        self.cities = []

    def add_city(self, city):
        """Add a city"""
        if not isinstance(city, City):
            raise TypeError("The city must be an instance of the City class")
        self.cities.append(city)

    @property
    def name(self):
        """Get the name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the name"""
        if not isinstance(value, str):
            raise ValueError("The name must be a string")
        if not value.strip():
            raise ValueError("The name cannot be blank")
        self.__name = value

    @classmethod
    def create(cls, name):
        """Create a new country"""
        country = cls(name)
        cls.DataManager.save(country)
        return country

    @classmethod
    def get(cls, name):
        """Get a specific country by name"""
        return cls.DataManager.get(name, "Country")

    def update(self):
        """Update country data"""
        self.DataManager.update(self)

    def delete(self):
        """Delete country"""
        self.DataManager.delete(self.__name, "Country")

    @classmethod
    def all(cls):
        """Retrieve all countries"""
        return cls.DataManager.all("Country")
