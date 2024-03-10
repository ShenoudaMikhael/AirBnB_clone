#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittests for testing init of Console"""

    def test_empty_input(self):
        """Test empty line input"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue())


if __name__ == "__main__":
    unittest.main()
