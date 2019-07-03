#!/usr/bin/python3
"""Module to define the User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class for HBNB"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
