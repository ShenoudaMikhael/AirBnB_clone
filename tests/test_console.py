#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import cmd


class TestConsole(unittest.TestCase):
    """Unittests for testing init of Console"""

    def test_cmd_type(self):
        """cmd type test"""

        self.assertEqual(HBNBCommand().__class__.__base__, cmd.Cmd)

    def test_class_name(self):
        """cmd type test"""
        self.assertEqual(HBNBCommand().__class__.__name__, "HBNBCommand")

    def test_EOF(self):
        """Test empty line input"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_quit(self):
        """Test empty line input"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_empty_input(self):
        """Test empty line input"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_help_exists(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")

        self.assertNotEqual(f.getvalue(), "name 'help' is not defined\n")
        self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_custom_prompt(self):
        with patch("sys.stdout", new=StringIO()) as f:
            prompt = HBNBCommand().prompt

        self.assertEqual(prompt, "(hbnb) ")


if __name__ == "__main__":
    unittest.main()
