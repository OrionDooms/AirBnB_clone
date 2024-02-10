#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
import os


class FileStorage():
    """Define filestorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        The obj with key <obj class name>.id set in FileStorage__objects
        """
        class_name = obj.__class__.__name__
        object_id = obj.id
        key = "{}.{}".format(object_id, class_name)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes FileStorage__objects to the JSON file (path: __file_path)
        """
        save_dict = {}
        for object_key, object_instance in FileStorage.__objects.items():
            save_dict[object_key] = object_instance.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(save_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to FileStorage__objects
        and only if the JSON file __file_path exists
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                FileStorage.__objects = data
