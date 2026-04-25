#!/usr/bin/python3
"""defines a Place class"""

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity

class Place(BaseModel):
    """defines a Place class"""
    def __init__(self, title, description, price, latitude, longitude, owner):
        """initilizes the Place class"""
        super().__init__()

        if title is None or not isinstance(title, str):
            raise ValueError("title must be a string")
        if title.strip() == "":
            raise ValueError("title cannot be empty")
        if len(title) > 100:
            raise ValueError("title must be at most 100 characters")

        if description is not None and not isinstance(description, str):
            raise ValueError("description must be a string")

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("price must be a number")
        if price <= 0:
            raise ValueError("price must be a positive value")

        if isinstance(latitude, bool) or not isinstance(latitude, (int, float)):
            raise ValueError("latitude must be a number")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("latitude must be between -90.0 and 90.0")

        if isinstance(longitude, bool) or not isinstance(longitude, (int, float)):
            raise ValueError("longitude must be a number")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("longitude must be between -180.0 and 180.0")

        if owner is None or not isinstance(owner, User):
            raise ValueError("owner must be a valid User instance")

        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """adds a review to the place"""
        if review not in self.reviews:
            self.reviews.append(review)
            self.save()

    def add_amenity(self, amenity):
        """adds an amenity to the place"""
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be an Amenity instance")
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.save()
