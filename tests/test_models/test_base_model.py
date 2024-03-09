#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """Unittests for testing init of User class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        """each id is unique"""
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        """different time when create"""
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertLess(user1.updated_at, user2.updated_at)


class test_BaseModel_save(unittest.TestCase):
    """Unittests for save"""

    def test_save(self):
        instance = BaseModel()
        data = instance.updated_at
        instance.save()
        self.assertNotEqual(data, instance.updated_at)

    def test_save_updates_file(self):
        instance = BaseModel()
        instance.save()
        instanceid = "BaseModel.{}".format(instance.id)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(instanceid, f.read())


class test_BaseModel_to_dict(unittest.TestCase):
    """Unittests for to_dict"""

    def test_to_dict(self):
        instance = BaseModel()
        data = instance.to_dict()
        self.assertEqual(dict, type(data))

    def test_to_dict_keys(self):
        instance = BaseModel()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())
        self.assertIn("__class__", instance.to_dict())


if __name__ == "__main__":
    unittest.main()
