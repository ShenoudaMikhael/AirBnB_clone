import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """setUp"""
        self.console = HBNBCommand()

    def test_quit_command(self):
        """test_quit_command"""
        with self.assertRaises(SystemExit):

            self.assertTrue(self.console.onecmd("quit"))

    def test_eof_command(self):
        """test_eof_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_help_command(self):
        """test_help_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_custom_prompt(self):
        """test_custom_prompt"""
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_empty_line(self):
        """test_empty_line"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(""))
            self.assertEqual(f.getvalue().strip(), "")


if __name__ == "__main__":
    unittest.main()
