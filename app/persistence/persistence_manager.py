from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """Save an entity."""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """Retrieve an entity by its ID and type."""
        pass

    @abstractmethod
    def update(self, entity):
        """Update an existing entity."""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """Delete an entity by its ID and type."""
        pass

    @abstractmethod
    def get_all(self, entity_type):
        """Retrieve all entities of a specific type."""
        pass
