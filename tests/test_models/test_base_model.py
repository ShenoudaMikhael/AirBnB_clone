#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class test_BaseModel_init(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
