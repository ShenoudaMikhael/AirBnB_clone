#!/usr/bin/python3
"""unittest for user.py"""
import unittest
from models.city import City
from datetime import datetime


class test_init_City(unittest.TestCase):
    """Unittests for testing init of City class"""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_name(self):
        """name is a string"""
        self.assertEqual(str, type(City.name))


    def test_unique_id(self):
        """each id is unique"""
        user1 = City()
        user2 = City()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        """different time when create"""
        user1 = City()
        user2 = City()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        user1 = City()
        user2 = City()
        self.assertLess(user1.updated_at, user2.updated_at)
    
class test_User_save(unittest.TestCase):
    """Unittests for save"""
    
    def test_save(self):
        instance = City()
        data = instance.updated_at
        instance.save()
        self.assertNotEqual(data, instance.updated_at)

if __name__ == "__main__":
    unittest.main()
