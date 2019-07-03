#!/usr/bin/python3
"""Module containing tests for the State class"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_inherit(self):
        """Tests that State class inherits from BaseModel class"""

        new = State()
        self.assertIsInstance(new, BaseModel)

    def test_attr(self):
        """Tests State class 'name' attribute"""

        new = State()
        self.assertTrue("name" in new.__dir__())

    def test_attrString(self):
        """Tests that 'name' attribute is type(str)"""

        new = State()
        name = getattr(new, "name")
        self.assertIsInstance(name, str)
