#!/usr/bin/python3
# Abstract base class for persistence managers

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """Save an entity to the storage."""
        pass

    @abstractmethod
    def get(self, entity_id):
        """Retrieve an entity from the storage by its ID."""
        pass

    @abstractmethod
    def update(self, entity_id, new_data):
        """Update an existing entity in the storage."""
        pass

    @abstractmethod
    def delete(self, entity_id):
        """Delete an entity from the storage by its ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieve all entities from the storage."""
        pass
