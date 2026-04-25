#!/usr/bin/python3
"""defines a Review class"""

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    """defines a Review class"""
    def __init__(self, text, rating, place, user):
        if text is None or not isinstance(text, str):
            raise ValueError("text must be a string")
        if text.strip() == "":
            raise ValueError("text cannot be empty")

        if isinstance(rating, bool) or not isinstance(rating, int):
            raise ValueError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")

        if place is None or not isinstance(place, Place):
            raise ValueError("place must be a valid Place instance")

        if user is None or not isinstance(user, User):
            raise ValueError("user must be a valid User instance")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
