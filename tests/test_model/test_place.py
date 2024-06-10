import unittest
from models.place import Place
from models.user import User


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.user = User("host@example.com", "password", "Host", "User")
        self.place = Place(
            name="Cozy Cottage",
            description="A small, cozy cottage in the woods.",
            address="123 Forest Lane",
            city_id="1",
            latitude=40.7128,
            longitude=-74.0060,
            host=self.user,
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=4
        )
        self.user.host_place(self.place)
        self.guest = User("guest@example.com", "password", "Guest", "User")

    def test_place_creation(self):
        """
        Test the creation of a Place object.
        """
        self.assertEqual(self.place.name, "Cozy Cottage")
        self.assertEqual(self.place.description, "A small, cozy cottage in the woods.")
        self.assertEqual(self.place.address, "123 Forest Lane")
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.host_id, self.user.id)
        self.assertEqual(self.place.number_of_rooms, 2)
        self.assertEqual(self.place.number_of_bathrooms, 1)
        self.assertEqual(self.place.price_per_night, 100)
        self.assertEqual(self.place.max_guests, 4)

    def test_to_dict(self):
        """
        Test the to_dict method of Place.
        """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['name'], "Cozy Cottage")
        self.assertEqual(place_dict['description'], "A small, cozy cottage in the woods.")
        self.assertEqual(place_dict['address'], "123 Forest Lane")
        self.assertEqual(place_dict['city_id'], "1")
        self.assertEqual(place_dict['latitude'], 40.7128)
        self.assertEqual(place_dict['longitude'], -74.0060)
        self.assertEqual(place_dict['host_id'], self.user.id)
        self.assertEqual(place_dict['number_of_rooms'], 2)
        self.assertEqual(place_dict['number_of_bathrooms'], 1)
        self.assertEqual(place_dict['price_per_night'], 100)
        self.assertEqual(place_dict['max_guests'], 4)

    def test_update_place(self):
        """
        Test updating attributes of a Place.
        """
        self.place.name = "Lakeside Cabin"
        self.place.description = "A cabin by the lake."
        self.place.save()
        self.assertEqual(self.place.name, "Lakeside Cabin")
        self.assertEqual(self.place.description, "A cabin by the lake.")

    def test_place_unique_id(self):
        """
        Test that each place has a unique ID.
        """
        place2 = Place(
            name="Mountain Retreat",
            description="A cabin in the mountains.",
            address="456 Mountain Road",
            city_id="2",
            latitude=35.6895,
            longitude=139.6917,
            host=self.user,
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=200,
            max_guests=6
        )
        self.assertNotEqual(self.place.id, place2.id)

    def test_add_booking(self):
        """
        Test adding a booking to a place.
        """
        self.place.add_booking(self.guest)
        self.assertIn(self.guest, self.place.bookings)


if __name__ == '__main__':
    unittest.main()
