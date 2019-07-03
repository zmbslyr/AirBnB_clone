#!/usr/bin/python3
"""Module containing tests for Amenity class"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests Amenity class"""

    def test_inherit(self):
        """Tests that Amenity class inherits from BaseModel"""

        new = Amenity()
        self.assertIsInstance(new, BaseModel)

    def test_attr(self):
        """Tests Amenity class 'name' attribute"""

        new = Amenity()
        self.assertTrue("name" in new.__dir__())

    def test_attrString(self):
        """Tests that 'name' attribute is type(str)"""

        new = Amenity()
        name = getattr(new, "name")
        self.assertIsInstance(name, str)
