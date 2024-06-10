from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    Interface for a persistence manager that defines the standard operations
    for saving, retrieving, updating, and deleting entities. This interface
    enforces a consistent approach to data management across
    different types of
    storage mechanisms.
    """

    @abstractmethod
    def save(self, entity):
        """
        Save an entity to the storage.

        Args:
            entity: The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity from the storage by its ID and type.

        Args:
            entity_id: The ID of the entity to retrieve.
            entity_type: The type of the entity to retrieve.

        Returns:
            The retrieved entity.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an existing entity in the storage.

        Args:
            entity: The entity with updated information.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the storage by its ID and type.

        Args:
            entity_id: The ID of the entity to delete.
            entity_type: The type of the entity to delete.
        """
        pass
