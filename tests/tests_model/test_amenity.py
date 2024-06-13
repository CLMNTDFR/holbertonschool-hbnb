#!/usr/bin/python3
import unittest
from datetime import datetime
from model.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Créer une instance d'Amenity pour une utilisation dans les tests
        self.amenity = Amenity("Piscine")

    def test_creation_amenity(self):
        # Vérifier que l'amenity a été créée avec le nom correct
        self.assertEqual(self.amenity.name, "Piscine")

        # Vérifier que l'amenity a un identifiant non vide
        self.assertTrue(self.amenity.amenity_id)

        # Vérifier que les horodatages de création et de mise à jour sont définis et qu'ils sont proches dans le temps
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertAlmostEqual((self.amenity.updated_at - self.amenity.created_at).total_seconds(), 0, delta=1)

    def test_to_dict(self):
        # Vérifier que la méthode to_dict renvoie un dictionnaire contenant les bonnes clés
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('amenity_id', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

        # Vérifier que les valeurs du dictionnaire correspondent aux attributs de l'amenity
        self.assertEqual(amenity_dict['name'], self.amenity.name)
        self.assertEqual(amenity_dict['amenity_id'], self.amenity.amenity_id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at)
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
