#!/usr/bin/python3
"""unittest for user.py"""
import unittest
from models.user import User
from datetime import datetime


class test_init_user(unittest.TestCase):
    """Unittests for testing init of User class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        """email is a string"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """password is a string"""
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """firt_name is a string"""
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """last_name is a string"""
        self.assertEqual(str, type(User.last_name))

    def test_unique_id(self):
        """each id is unique"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        """different time when create"""
        user1 = User()
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        user1 = User()
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)
    
class test_User_save(unittest.TestCase):
    """Unittests for save"""
    
    def test_save(self):
        instance = User()
        data = instance.updated_at
        instance.save()
        self.assertNotEqual(data, instance.updated_at)

if __name__ == "__main__":
    unittest.main()
