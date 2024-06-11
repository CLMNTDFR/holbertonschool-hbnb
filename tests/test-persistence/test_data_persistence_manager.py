import unittest
from Persistence.DataManager import DataManager
from Persistence.IPersistenceManager import IPersistenceManager

# Création de classes d'entités factices pour le test


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Place:
    def __init__(self, id, location):
        self.id = id
        self.location = location


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.user = User(id=1, name="Alice")
        self.place = Place(id=2, location="Paris")

    def test_save_entity(self):
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)
        self.assertEqual(self.data_manager.get(1, "User").name, "Alice")
        self.assertEqual(self.data_manager.get(2, "Place").location, "Paris")

    def test_get_entity(self):
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)
        retrieved_user = self.data_manager.get(1, "User")
        retrieved_place = self.data_manager.get(2, "Place")
        self.assertIsNotNone(retrieved_user)
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_user.name, "Alice")
        self.assertEqual(retrieved_place.location, "Paris")

    def test_update_entity(self):
        self.data_manager.save(self.user)
        self.user.name = "Bob"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(1, "User")
        self.assertEqual(updated_user.name, "Bob")

    def test_delete_entity(self):
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)
        self.data_manager.delete(1, "User")
        self.data_manager.delete(2, "Place")
        self.assertIsNone(self.data_manager.get(1, "User"))
        self.assertIsNone(self.data_manager.get(2, "Place"))

    def test_get_non_existent_entity(self):
        self.assertIsNone(self.data_manager.get(999, "User"))

    def test_update_non_existent_entity(self):
        non_existent_user = User(id=999, name="Ghost")
        self.data_manager.update(non_existent_user)
        self.assertIsNone(self.data_manager.get(999, "User"))

    def test_delete_non_existent_entity(self):
        self.data_manager.delete(999, "User")
        self.assertIsNone(self.data_manager.get(999, "User"))


if __name__ == "__main__":
    unittest.main()
