#!/usr/bin/python3
"""Base model Module"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """Class Base contains only Id, Creation date, update date."""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            return
        self.id = uuid.uuid4().__str__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def update_atts(self, att, val, **kwarg):
        """update object"""

        print("AAAA")
        print(kwarg)

        if att not in ["id", "created_at", "updated_at"]:
            setattr(self, att, val)
            self.save()

    def save(self):
        """base function for saving"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """serilize model to dict object"""
        base_dict = self.__dict__.copy()
        base_dict["updated_at"] = datetime.strftime(
            base_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        base_dict["created_at"] = datetime.strftime(
            base_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        base_dict["__class__"] = self.__class__.__name__
        return base_dict

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    @classmethod
    def show(cls, id=""):
        """return show function format"""
        return ["show", " ".join([cls.__name__, id])]

    @classmethod
    def all(cls, id=""):
        """return all function format"""
        return ["all", " ".join([cls.__name__, id])]

    @classmethod
    def destroy(cls, id=""):
        """return destroy function format"""
        return ["destroy", " ".join([cls.__name__, id])]

    @classmethod
    def create(cls, id=""):
        """return create function format"""
        return ["create", " ".join([cls.__name__, id])]

    @classmethod
    def count(cls, id=""):
        """return count function format"""
        return ["count", " ".join([cls.__name__, id])]

    @classmethod
    def update(cls, id="", att="", prop="", **kwarg):
        """return update function format"""
        if len(kwarg) > 0:
            return ["update", " ".join([cls.__name__, id, {**prop}])]
            
        return ["update", " ".join([cls.__name__, id, att, prop])]
