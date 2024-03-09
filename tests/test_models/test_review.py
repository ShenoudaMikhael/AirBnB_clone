#!/usr/bin/python3
"""unittest for user.py"""
import unittest
from models.review import Review
from datetime import datetime


class test_init_Review(unittest.TestCase):
    """Unittests for testing init of Review class"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_text(self):
        """name is a string"""
        self.assertEqual(str, type(Review.text))


    def test_different_created_at(self):
        """different time when create"""
        user1 = Review()
        user2 = Review()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        user1 = Review()
        user2 = Review()
        self.assertLess(user1.updated_at, user2.updated_at)
    
class test_Review_save(unittest.TestCase):
    """Unittests for save"""
    
    def test_save(self):
        instance = Review()
        data = instance.updated_at
        instance.save()
        self.assertNotEqual(data, instance.updated_at)

    
if __name__ == "__main__":
    unittest.main()
