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


class test_City_save(unittest.TestCase):
    """Unittests for save"""

    def test_save(self):
        instance = City()
        data = instance.updated_at
        instance.save()
        self.assertNotEqual(data, instance.updated_at)


class test_City_to_dict(unittest.TestCase):
    """Unittests for to_dict"""

    def test_to_dict_attrs(self):
        """test all attributes"""
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_strs(self):
        """test strings in the dictionary"""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        """to dect function test"""
        dt = datetime.now()
        city = City()
        city.id = "1"
        city.updated_at = city.created_at = dt
        mdict = {
            "id": "1",
            "__class__": "City",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), mdict)


if __name__ == "__main__":
    unittest.main()
