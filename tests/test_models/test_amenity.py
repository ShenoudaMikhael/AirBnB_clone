#!/usr/bin/python3
"""unittest for state.py"""

import unittest
from datetime import datetime
from models.amenity import Amenity


class test_init_Amenity(unittest.TestCase):
    """Unittests for testing init of Amenity class"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name(self):
        """name is a string"""
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)

    def test_unique_id(self):
        """each id is unique"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_different_created_at(self):
        """different time when create"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_no_args_sec(self):
        """test no args"""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_kwargs(self):
        """test dict"""
        dictt = datetime.now()
        dictt_iso = dictt.isoformat()
        amenity = Amenity(id="1", created_at=dictt_iso, updated_at=dictt_iso)
        self.assertEqual(amenity.id, "1")
        self.assertEqual(amenity.created_at, dictt)
        self.assertEqual(amenity.updated_at, dictt)

    def test_no_kwargs(self):
        """test no kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class test_Amenity_save(unittest.TestCase):
    """Unittests for save"""

    def test_save(self):
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
