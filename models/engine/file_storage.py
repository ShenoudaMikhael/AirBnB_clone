#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """File Storage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        try:
            with open(
                    "{}".format(self.__file_path),
                    'r', encoding='utf-8') as file:
                q = file.read()
                print("AAAAA")
                self.__objects = json.loads(q)
            return self.__objects
        except FileNotFoundError:
            return self.__objects

    def new(self, obj):
        """add new obj to objects dictionary"""
        self.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """Save objects to a file."""

        with open(
                "{}".format(self.__file_path), "w+", encoding="utf-8") as file:
            if self.__objects is not None:
                file.write(json.dumps(self.__objects))
            else:
                file.write(json.dumps([]))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(
                    "{}".format(self.__file_path),
                    "r", encoding="utf-8") as file:
                items = json.loads(file.read())
                if not items:
                    return
                self.__objects = items
        except FileNotFoundError:
            pass
