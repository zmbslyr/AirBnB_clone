#!/usr/bin/python3
"""Module containing tests for Review class"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def test_inherit(self):
        """Tests that Review class inherits from BaseModel"""

        new = Review()
        self.assertIsInstance(new, BaseModel)

    def test_attrs(self):
        """Tests that attributes exist in Review class"""

        new = Review()
        self.assertTrue("place_id" in new.__dir__())
        self.assertTrue("user_id" in new.__dir__())
        self.assertTrue("text" in new.__dir__())

    def test_placeType(self):
        """Tests that attribute 'place_id' is type(str)"""

        new = Review()
        place = getattr(new, "place_id")
        self.assertIsInstance(place, str)

    def test_userType(self):
        """Tests that attribute 'user_id' is type(str)"""

        new = Review()
        place = getattr(new, "user_id")
        self.assertIsInstance(place, str)

    def test_textType(self):
        """Tests that attribute 'text' is type(str)"""

        new = Review()
        text = getattr(new, "text")
        self.assertIsInstance(text, str)
