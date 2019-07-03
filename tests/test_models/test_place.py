#!/usr/bin/python3
"""Module containing tests for Place class"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for Place class"""

    def test_inherit(self):
        """Tests that Review class inherits from BaseModel"""

        new = Place()
        self.assertIsInstance(new, BaseModel)

    def test_attrs(self):
        """Tests that attributes exist in Place class"""

        new = Place()
        self.assertTrue("city_id" in new.__dir__())
        self.assertTrue("user_id" in new.__dir__())
        self.assertTrue("name" in new.__dir__())
        self.assertTrue("description" in new.__dir__())
        self.assertTrue("number_rooms" in new.__dir__())
        self.assertTrue("number_bathrooms" in new.__dir__())
        self.assertTrue("max_guest" in new.__dir__())
        self.assertTrue("price_by_night" in new.__dir__())
        self.assertTrue("latitude" in new.__dir__())
        self.assertTrue("longitude" in new.__dir__())
        self.assertTrue("amenity_ids" in new.__dir__())

    def test_cityType(self):
        """Tests that attribute 'city_id' is type(str)"""

        new = Place()
        city = getattr(new, "city_id")
        self.assertIsInstance(city, str)

    def test_userType(self):
        """Tests that attribute 'user_id' is type(str)"""

        new = Place()
        user = getattr(new, "user_id")
        self.assertIsInstance(user, str)

    def test_nameType(self):
        """Tests that attribute 'name' is type(str)"""

        new = Place()
        name = getattr(new, "name")
        self.assertIsInstance(name, str)

    def test_descType(self):
        """Tests that attribute 'description' is type(str)"""

        new = Place()
        desc = getattr(new, "description")
        self.assertIsInstance(desc, str)

    def test_roomType(self):
        """Tests that attribute 'number_rooms' is type(int)"""

        new = Place()
        room = getattr(new, "number_rooms")
        self.assertIsInstance(room, int)

    def test_bRoomType(self):
        """Tests that attribute 'number_bathrooms' is type(int)"""

        new = Place()
        bRoom = getattr(new, "number_bathrooms")
        self.assertIsInstance(bRoom, int)

    def test_guestType(self):
        """Tests that attribute 'max_guest' is type(int)"""

        new = Place()
        guest = getattr(new, "max_guest")
        self.assertIsInstance(guest, int)

    def test_priceType(self):
        """Tests that attribute 'price_by_night' is type(int)"""

        new = Place()
        price = getattr(new, "price_by_night")
        self.assertIsInstance(price, int)

    def test_latType(self):
        """Tests that attribute 'latitude' is type(float)"""

        new = Place()
        lat = getattr(new, "latitude")
        self.assertIsInstance(lat, float)

    def test_longType(self):
        """Tests that attribute 'longitude' is type(float)"""

        new = Place()
        lon = getattr(new, "longitude")
        self.assertIsInstance(lon, float)

    def test_amenType(self):
        """Tests that attribute 'amenity_ids' is type(list)"""

        new = Place()
        amen = getattr(new, "amenity_ids")
        self.assertIsInstance(amen, list)
