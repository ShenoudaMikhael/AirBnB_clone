#!/usr/bin/python3
"""unittest for state.py"""

import unittest
from datetime import datetime
from models.state import State


class test_init_State(unittest.TestCase):
    """Unittests for testing init of State class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id(self):
        """id is a string"""
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        """created_at is a datetime"""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        """updated_at is a datetime"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        """name is a string"""
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_unique_id(self):
        """each id is unique"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_at(self):
        """different time when create"""
        state1 = State()
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_different_updated_at(self):
        """different time when update"""
        state1 = State()
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_no_args(self):
        """test no args"""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_kwargs(self):
        """test dict"""
        dictt = datetime.now()
        dictt_iso = dictt.isoformat()
        st = State(id="1", created_at=dictt_iso, updated_at=dictt_iso)
        self.assertEqual(st.id, "1")
        self.assertEqual(st.created_at, dictt)
        self.assertEqual(st.updated_at, dictt)

    def test_no_kwargs(self):
        """test no kwargs"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class test_State_save(unittest.TestCase):
    """Unittests for save"""

    def test_save(self):
        state = State()
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)


if __name__ == "__main__":
    unittest.main()