import unittest
from datetime import datetime, timedelta
import uuid
from model.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.name = "Charming Cottage"
        self.description = "A lovely place to stay"
        self.address = "123 Main St"
        self.city_id = "CITY123"
        self.latitude = 48.8566
        self.longitude = 2.3522
        self.host_id = "HOST123"
        self.number_of_rooms = 3
        self.number_of_bathrooms = 2
        self.price_per_night = 100
        self.max_guests = 4
        self.amenity_ids = ["AMENITY1", "AMENITY2"]
        self.place = Place(
            self.name,
            self.description,
            self.address,
            self.city_id,
            self.latitude,
            self.longitude,
            self.host_id,
            self.number_of_rooms,
            self.number_of_bathrooms,
            self.price_per_night,
            self.max_guests,
            self.amenity_ids,
        )

    def test_place_creation(self):
        """Test if the place is created with correct attributes."""
        self.assertEqual(self.place.name, self.name)
        self.assertEqual(self.place.description, self.description)
        self.assertEqual(self.place.address, self.address)
        self.assertEqual(self.place.city_id, self.city_id)
        self.assertEqual(self.place.latitude, self.latitude)
        self.assertEqual(self.place.longitude, self.longitude)
        self.assertEqual(self.place.host_id, self.host_id)
        self.assertEqual(self.place.number_of_rooms, self.number_of_rooms)
        self.assertEqual(self.place.number_of_bathrooms,
                         self.number_of_bathrooms)
        self.assertEqual(self.place.price_per_night, self.price_per_night)
        self.assertEqual(self.place.max_guests, self.max_guests)
        self.assertEqual(self.place.amenity_ids, self.amenity_ids)
        self.assertIsInstance(self.place.place_id, str)
        self.assertTrue(uuid.UUID(self.place.place_id, version=4))
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertLessEqual(self.place.created_at, datetime.now())
        self.assertLessEqual(self.place.updated_at, datetime.now())
        self.assertEqual(self.place.reviews, [])

    def test_add_review(self):
        """Test adding a review."""
        review = "Great place!"
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)

    def test_calculate_total_price(self):
        """Test calculating the total price for a number of nights."""
        number_of_nights = 3
        expected_total_price = self.price_per_night * number_of_nights
        self.assertEqual(
            self.place.calculate_total_price(number_of_nights),
            expected_total_price
        )

    def test_list_amenities(self):
        """Test listing amenities."""
        self.assertEqual(self.place.list_amenities(), self.amenity_ids)

    def test_set_number_of_guests(self):
        """Test setting the number of guests."""
        new_max_guests = 5
        self.place.set_number_of_guests(new_max_guests)
        self.assertEqual(self.place.max_guests, new_max_guests)

    def test_add_description(self):
        """Test adding a description."""
        new_description = "A new description"
        self.place.add_description(new_description)
        self.assertEqual(self.place.description, new_description)

    def test_set_number_of_rooms(self):
        """Test setting the number of rooms."""
        new_number_of_rooms = 4
        self.place.set_number_of_rooms(new_number_of_rooms)
        self.assertEqual(self.place.number_of_rooms, new_number_of_rooms)

    def test_set_location(self):
        """Test setting the location."""
        new_latitude = 40.7128
        new_longitude = -74.0060
        self.place.set_location(new_latitude, new_longitude)
        self.assertEqual(self.place.latitude, new_latitude)
        self.assertEqual(self.place.longitude, new_longitude)

    def test_add_amenity(self):
        """Test adding an amenity."""
        new_amenity = "AMENITY3"
        self.place.add_amenity(new_amenity)
        self.assertIn(new_amenity, self.place.amenity_ids)

    def test_delete_amenity(self):
        """Test deleting an amenity."""
        amenity_to_delete = "AMENITY1"
        self.place.delete_amenity(amenity_to_delete)
        self.assertNotIn(amenity_to_delete, self.place.amenity_ids)

    def test_update_place_data(self):
        """Test updating place data."""
        new_data = {"name": "New Name", "number_of_rooms": 5}
        self.place.update_place_data(new_data)
        self.assertEqual(self.place.name, "New Name")
        self.assertEqual(self.place.number_of_rooms, 5)
        self.assertLessEqual(self.place.updated_at, datetime.now())

    def test_to_dict(self):
        """Test the to_dict method."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["place_id"], self.place.place_id)
        self.assertEqual(place_dict["name"], self.place.name)
        self.assertEqual(place_dict["description"], self.place.description)
        self.assertEqual(place_dict["address"], self.place.address)
        self.assertEqual(place_dict["city_id"], self.place.city_id)
        self.assertEqual(place_dict["latitude"], self.place.latitude)
        self.assertEqual(place_dict["longitude"], self.place.longitude)
        self.assertEqual(place_dict["host_id"], self.place.host_id)
        self.assertEqual(place_dict["number_of_rooms"],
                         self.place.number_of_rooms)
        self.assertEqual(
            place_dict["number_of_bathrooms"],
            self.place.number_of_bathrooms
        )
        self.assertEqual(place_dict["price_per_night"],
                         self.place.price_per_night)
        self.assertEqual(place_dict["max_guests"], self.place.max_guests)
        self.assertEqual(place_dict["amenity_ids"], self.place.amenity_ids)
        self.assertEqual(place_dict["reviews"], self.place.reviews)
        self.assertEqual(place_dict["created_at"], self.place.created_at)
        self.assertEqual(place_dict["updated_at"], self.place.updated_at)


if __name__ == "__main__":
    unittest.main()
