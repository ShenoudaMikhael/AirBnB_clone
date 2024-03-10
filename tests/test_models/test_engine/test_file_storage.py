#!/usr/bin/python3
"""Defines unittests for file_storage.py."""

import models
import unittest
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

    def test_all_empty(self):
        objects = FileStorage().all()
        self.assertEqual(objects, {})

    def test_filestorage_init(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_private_str(self):
        self.assertEqual(str, type(models.storage._FileStorage__file_path))

    def test_private_dict(self):
        self.assertEqual(dict, type(models.storage._FileStorage__objects))


class test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing FileStorage methods"""

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)
            FileStorage(None)

    def test_new(self):
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
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
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
        ""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
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


if __name__ == "__main__":
    unittest.main()
