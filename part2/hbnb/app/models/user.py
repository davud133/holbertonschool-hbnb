#!/usr/bin/python3
"""defines User class"""

from app.models.base_model import BaseModel

class User(BaseModel):
    """defines User class"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        """initilizes the User"""
        super().__init__()
        if first_name is None or not isinstance(first_name, str):
            raise ValueError("first_name must be a string")
        if first_name.strip() == "":
            raise ValueError("first_name cannot be empty")
        if len(first_name) > 50:
            raise ValueError("first_name must be at most 50 characters")

        if last_name is None or not isinstance(last_name, str):
            raise ValueError("last_name must be a string")
        if last_name.strip() == "":
            raise ValueError("last_name cannot be empty")
        if len(last_name) > 50:
            raise ValueError("last_name must be at most 50 characters")

        if email is None or not isinstance(email, str):
            raise ValueError("email must be a string")
        if email.strip() == "":
            raise ValueError("email cannot be empty")
        if "@" not in email or email.startswith("@") or email.endswith("@"):
            raise ValueError("email must be a valid email address")

        if not isinstance(is_admin, bool):
            raise ValueError("is_admin must be a boolean")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
