import json
import os
from datetime import datetime
from app.persistence.persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.file_path = "data.json"
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def _read_data(self):
        self._initialize_file()
        with open(self.file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _write_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def save(self, entity):
        self._initialize_file()
        data = self._read_data()
        entity_data = entity.to_dict()
        entity_type = entity.__class__.__name__
        entity_id = entity.id
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity_data
        self._write_data(data)

    def get(self, entity_id, entity_type):
        self._initialize_file()
        data = self._read_data()
        return data.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        self.save(entity)

    def delete(self, entity_id, entity_type):
        self._initialize_file()
        data = self._read_data()
        if entity_type in data and entity_id in data[entity_type]:
            del data[entity_type][entity_id]
            self._write_data(data)

    def get_all(self, entity_type):
        self._initialize_file()
        data = self._read_data()
        return list(data.get(entity_type, {}).values())

    def clear(self, entity_type):
        data = self._read_data()
        if entity_type in data:
            data[entity_type] = {}
            self._write_data(data)
