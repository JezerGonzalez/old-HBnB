from .Interface import IPersistenceManager


class DataManager(IPersistenceManager):
    """DataManager class"""

    def __init__(self):
        """Initialize DataManager"""
        self.storage = {
            "User": {},
            "City": {},
            "Amenity": {},
            "Place": {},
            "Review": {},
        }

    def save(self, entity):
        """save data"""
        data_type = type(entity).__name__
        if data_type not in self.storage:
            raise ValueError(f"Invalid data type: {data_type}")
        self.storage[data_type][entity.id] = entity

    def get(self, entity_id, entity_type):
        """Get the data for a given entity"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        return self.storage[entity_type][entity_id]

    def update(self, entity):
        """Update the data for a given entity"""
        data_type = type(entity).__name__
        if data_type not in self.storage:
            raise ValueError(f"Invalid data type: {data_type}")
        if entity.id in self.storage[data_type]:
            self.storage[data_type][entity.id] = entity
        else:
            raise ValueError(f"Entity {entity} does not exist")

    def delete(self, entity_id, entity_type):
        """Delete a entity from the database"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
        else:
            raise ValueError(f"Entity {entity_type} does not exist")

    def all_entities(self, entity_type):
        """Returns a list of all entities"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        return list(self.storage[entity_type].values())
