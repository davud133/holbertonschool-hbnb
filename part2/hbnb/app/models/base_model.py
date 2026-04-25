#!/usr/bin/python3
"""defines a Base class for models"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the Updated at timestamp whenever the object is updated"""
        self.updated_at = datetime.now()
    def update(self, data):
        """Update the attributes of object based on the given dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
