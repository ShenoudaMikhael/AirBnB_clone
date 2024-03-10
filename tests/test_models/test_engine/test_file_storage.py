#!/usr/bin/python3
"""Defines unittests for file_storage.py."""

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class test_init_file_storage(unittest.TestCase):
    """Unittests for testing init"""

    def setUp(self):
        """setUp"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_empty(self):
        """test_all_empty"""
        objects = FileStorage().all()
        self.assertEqual(type(objects), dict)

    def test_filestorage_init(self):
        """test_filestorage_init"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_init(self):
        """test_storage_init"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_private_str(self):
        """test_private_str"""
        self.assertEqual(str, type(models.storage._FileStorage__file_path))

    def test_private_dict(self):
        """test_private_dict"""
        self.assertEqual(dict, type(models.storage._FileStorage__objects))


class test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing FileStorage methods"""

    def test_all(self):
        """test_all"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_arg(self):
        """test_arg"""
        with self.assertRaises(TypeError):
            models.storage.all(None)
            FileStorage(None)

    def test_new(self):
        """test_new"""
        basemodel = BaseModel()
        user = User()
        city = City()
        place = Place()
        state = State()
        review = Review()
        amenity = Amenity()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(review)
        models.storage.new(amenity)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())

    def test_none(self):
        """test_none"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """test_save"""
        basemodel = BaseModel()
        user = User()
        city = City()
        place = Place()
        state = State()
        review = Review()
        amenity = Amenity()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(review)
        models.storage.new(amenity)
        models.storage.save()
        text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + basemodel.id, text)
            self.assertIn("User." + user.id, text)
            self.assertIn("State." + state.id, text)
            self.assertIn("Place." + place.id, text)
            self.assertIn("City." + city.id, text)
            self.assertIn("Amenity." + amenity.id, text)
            self.assertIn("Review." + review.id, text)

    def test_arg_sec(self):
        """test_arg_sec"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """test_reload"""
        basemodel = BaseModel()
        user = User()
        city = City()
        place = Place()
        state = State()
        review = Review()
        amenity = Amenity()

        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(review)
        models.storage.new(amenity)

        models.storage.save()

        models.storage.reload()

        objs = models.storage._FileStorage__objects

        self.assertIn("BaseModel." + basemodel.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)


class TestFileStorage(unittest.TestCase):
    """TestFileStorage"""
    def setUp(self):
        """setUp"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """tearDown"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialization(self):
        """test_initialization"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        """test_all"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        """test_new"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage._FileStorage__objects)

    def test_save_and_reload(self):
        """test_save_and_reload"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Check if the file exists after saving
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()

        self.assertIsInstance(all_objects, dict)
        self.assertIn("BaseModel.{}".format(obj.id), all_objects)

if __name__ == "__main__":
    unittest.main()
