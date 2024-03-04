#!/usr/bin/python3
"""File Storage Module"""


class FileStorage:
    """File Storage Class"""

    __file_path = "file.json"
    __objects = []

    def all(self):
        """return all objects"""
        return self.__objects

    def new(self, obj):
        self.__objects.append({obj.__class__.__name__: {obj}})

    def save(self):
        pass

    def reload(self):
        pass
