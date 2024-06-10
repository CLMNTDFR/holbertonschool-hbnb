from models.persistence_interface import IPersistenceManager
import json
import os


class DataManager(IPersistenceManager):
    """
    DataManager class implementing IPersistenceManager for
    file-based storage.
    """

    def __init__(self, storage_file='data.json'):
        """
        Initialize DataManager with a specified storage file.
        """
        self.storage_file = storage_file
        self._load_storage()

    def _load_storage(self):
        """
        Load storage data from the storage file.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                self.storage = json.load(file)
        else:
            self.storage = {}

    def _save_storage(self):
        """
        Save storage data to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.storage, file)

    def save(self, entity):
        """
        Save an entity to storage.
        """
        entity_id = entity.get('id')
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity
        self._save_storage()

    def get(self, entity_id, entity_type):
        """
        Retrieve an entity from storage by ID and type.
        """
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        """
        Update an existing entity in storage.
        """
        entity_id = entity.get('id')
        entity_type = type(entity).__name__
        if entity_type in self.storage and \
                entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            self._save_storage()

    def delete(self, entity_id, entity_type):
        """
        Delete an entity from storage by ID and type.
        """
        if entity_type in self.storage and \
                entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self._save_storage()
