import unittest
import json, os

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):
    def setUp(self):
        """setUp"""
        self.console = HBNBCommand()
        try:
            os.remove("file.json")
        except Exception:
            pass

    def tearDown(self):
        """
        Remove temporary file (file.json) created as a result
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_quit_command(self):
        """test_quit_command"""
        with self.assertRaises(SystemExit):

            self.assertTrue(self.console.onecmd("quit"))

    def test_eof_command(self):
        """test_eof_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_docstrings(self):
        """checking for docstrings"""
        self.assertIsNotNone(self.console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_wrong_command(self):
        """test_eof_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("wrongComand")
            self.assertEqual(f.getvalue().strip(), "name 'wrongComand' is not defined")

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

    def test_all_command(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all"))
            for item in json.loads(f.getvalue().strip()):
                models = [
                    "[User]",
                    "[BaseModel]",
                    "[City]",
                    "[Amenity]",
                    "[Place]",
                    "[Review]",
                    "[State]",
                ]
                self.assertIn(item.split()[0], models)

    def test_all_with_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all BaseModel"))

            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[BaseModel]")

    def test_all_with_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_command(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        with patch("sys.stdout", new=StringIO()) as f:
            instance = BaseModel()
            self.assertFalse(self.console.onecmd(f"update BaseModel {instance.id}"))
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        with patch("sys.stdout", new=StringIO()) as f:
            instance = BaseModel()
            self.assertFalse(
                self.console.onecmd(f"update BaseModel {instance.id} email")
            )
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    # BaseModel value cases
    def test_command_create_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn(f"BaseModel.{output}", storage.all().keys())

    def test_command_create_User(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertIn(f"User.{output}", storage.all().keys())

    def test_command_create_City(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue().strip()
            self.assertIn(f"City.{output}", storage.all().keys())

    def test_command_create_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue().strip()
            self.assertIn(f"Amenity.{output}", storage.all().keys())

    def test_command_create_Place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue().strip()
            self.assertIn(f"Place.{output}", storage.all().keys())

    def test_command_create_Review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue().strip()
            self.assertIn(f"Review.{output}", storage.all().keys())

    def test_command_create_State(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            self.assertIn(f"State.{output}", storage.all().keys())

    def test_command_count_User(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(
                output, str(len([
                    k for k in storage.all() if k.split(".")[0] == "User"]))
            )


if __name__ == "__main__":
    unittest.main()
