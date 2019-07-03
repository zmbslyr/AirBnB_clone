#!/usr/bin/python3
"""Module containing tests for City class"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def test_inherit(self):
        """Tests that City class inherits from BaseModule"""

        new = City()
        self.assertIsInstance(new, BaseModel)

    def test_attrs(self):
        """Tests that attributes exist in City class"""

        new = City()
        self.assertTrue("state_id" in new.__dir__())
        self.assertTrue("name" in new.__dir__())

    def test_stateType(self):
        """Tests that attribute 'state_id' is type(str)"""

        new = City()
        state = getattr(new, "state_id")
        self.assertIsInstance(state, str)

    def test_nameType(self):
        """Tests that attribute 'name' is type(str)"""

        new = City()
        name = getattr(new, "name")
        self.assertIsInstance(name, str)
