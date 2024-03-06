#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """File Storage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return self.__objects

    def new(self, obj):
        """add new obj to objects dictionary"""
        self.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def destroy(self, obj_id):
        """add new obj to objects dictionary"""
        self.__objects.pop(obj_id)
        self.save()

    def save(self):
        """Save objects to a file."""

        with open(
                "{}".format(self.__file_path), "w+", encoding="utf-8") as file:
            if self.__objects is not None:
                file.write(json.dumps(
                    {k: self.__objects[k].to_dict() for k in self.__objects},
                    indent=4))
            else:
                file.write(json.dumps([]))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        class_list = {
            "BaseModel": BaseModel,
            "User": User
            }

        try:
            with open(
                    "{}".format(self.__file_path),
                    "r", encoding="utf-8") as file:
                items = json.loads(file.read())
                if not items:
                    return
                self.__objects = {
                    k: class_list[k.split('.')[0]](**items[k]) for k in items}
        except FileNotFoundError:
            pass
