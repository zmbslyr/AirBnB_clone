#!/usr/bin/python3
"""Module to define Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for HBNB"""

    place_id = ""
    user_id = ""
    text = ""
