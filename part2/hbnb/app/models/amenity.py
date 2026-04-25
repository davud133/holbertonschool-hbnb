#!/usr/bin/python3
"""defines Amenity class"""

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """defines Amenity class"""

    def __init__(self, name):
        """initializes the Amenity"""
        super().__init__()

        if name is None or not isinstance(name, str):
            raise ValueError("name must be a string")
        if name.strip() == "":
            raise ValueError("name cannot be empty")
        if len(name) > 50:
            raise ValueError("name must be at most 50 characters")

        self.name = name
