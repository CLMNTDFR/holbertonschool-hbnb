from .IPersistenceManager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    DataManager class that implements the IPersistenceManager interface
    to manage data persistence. This class handles CRUD operations for
    various types of entities using an in-memory storage for demonstration.
    """

    def __init__(self):
        # In-memory storage represented as a dictionary of dictionaries.
        # The outer dictionary's keys are entity types, and the inner
        # dictionaries' keys are entity IDs.
        self.storage = {}

    def save(self, entity):
        """
        Save an entity to the in-memory storage.

        Args:
            entity: The entity to be saved.
        """
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id, entity_type):
        """
        Retrieve an entity from the in-memory storage by its ID and type.

        Args:
            entity_id: The ID of the entity to retrieve.
            entity_type: The type of the entity to retrieve.

        Returns:
            The retrieved entity if found, None otherwise.
        """
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        """
        Update an existing entity in the in-memory storage.

        Args:
            entity: The entity with updated information.
        """
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the in-memory storage by its ID and type.

        Args:
            entity_id: The ID of the entity to delete.
            entity_type: The type of the entity to delete.
        """
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
