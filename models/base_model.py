#!/usr/bin/python3
"""BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel():
    """All attributes and methods of BaseModel class"""
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for a in ["created_at", "updated_at"]:
            if a in kwargs:
                kwargs[a] = datetime.strptime(kwargs[a], self.datetime_format)

        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)

    def __str__(self):
        """
        print out the class name, self.id, self.__dict__ .
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values.
        """
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)
