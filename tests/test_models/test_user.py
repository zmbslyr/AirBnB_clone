#!/usr/bin/python3
"""Module containing tests for User class"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def test_inherit(self):
        """Tests that User class inherits from BaseModel"""

        new = User()
        self.assertIsInstance(new, BaseModel)

    def test_attrs(self):
        """Tests that attributes exist in User class"""

        new = User()
        self.assertTrue("email" in new.__dir__())
        self.assertTrue("password" in new.__dir__())
        self.assertTrue("first_name" in new.__dir__())
        self.assertTrue("last_name" in new.__dir__())

    def test_emailType(self):
        """Tests that attribute 'email' is type(str)"""

        new = User()
        email = getattr(new, "email")
        self.assertIsInstance(email, str)

    def test_pwdType(self):
        """Tests that attribute 'password' is type(str)"""

        new = User()
        pwd = getattr(new, "password")
        self.assertIsInstance(pwd, str)

    def test_firstType(self):
        """Tests that attribute 'first_name' is type(str)"""

        new = User()
        first = getattr(new, "first_name")
        self.assertIsInstance(first, str)

    def test_lastType(self):
        """Tests that sttribute 'last_name' is type(str)"""

        new = User()
        last = getattr(new, "last_name")
        self.assertIsInstance(last, str)
