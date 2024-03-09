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


    def test_unique_id(self):
        """each id is unique"""
        place1 = Review()
        place2 = Review()
        self.assertNotEqual(place1.place_id, place2.place_id) 
        
    def test_unique_id(self):
        """each id is unique"""
        user1 = Review()
        user2 = Review()
        self.assertNotEqual(user1.user_id, user2.user_id)

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

class test_Review_to_dict(unittest.TestCase):
    """Unittests for to_dict"""
    
    def test_to_dict_attrs(self):
        """test all attributes"""
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_strs(self):
        """test strings in the dictionary"""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.now()
        review = Review()
        review.id = "1"
        review.updated_at = review.created_at = dt
        dict = {
            'id': '1',
            '__class__': 'review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), dict)
    
if __name__ == "__main__":
    unittest.main()
