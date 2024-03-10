import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from time import sleep


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

    # create
    def test_create_command(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_command(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_command(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


if __name__ == "__main__":
    unittest.main()
