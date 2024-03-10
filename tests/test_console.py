#!/usr/bin/python3
"""unittest for base_model.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

import cmd
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Unittests for testing init of Console
    """

    def test_cmd_type(self):
        """test_cmd_type
        """

        self.assertEqual(HBNBCommand().__class__.__base__, cmd.Cmd)

    def test_class_name(self):
        """test_class_name
        """
        self.assertEqual(HBNBCommand().__class__.__name__, "HBNBCommand")

    def test_EOF(self):
        """test_EOF
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_quit(self):
        """test_quit
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_empty_input(self):
        """test_empty_input
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_help_exists(self):
        """test_help_exists
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")

        self.assertNotEqual(f.getvalue(), "name 'help' is not defined\n")
        self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_custom_prompt(self):
        """test_custom_prompt
        """
        with patch("sys.stdout", new=StringIO()) as f:
            prompt = HBNBCommand().prompt

        self.assertEqual(prompt, "(hbnb) ")

    def test_create_no_arg(self):
        """test_create_no_arg
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_wrong_model(self):
        """test_create_wrong_model
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create unknownModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_user(self):
        """test_create_wrong_model
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertIn("User.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_show_no_arg(self):
        """test_show_no_arg
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_wrong_model(self):
        """test_show_wrong_model
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show UnknownModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_correct_model_no_id(self):
        """test_show_correct_model_no_id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_correct_model_wrong_id(self):
        """test_show_correct_model_wrong_id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123-123-13")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_show_correct_model_with_id(self):
        """test_show_correct_model_wrong_id
        """
        instance = BaseModel()
        instance_str = instance.__str__()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(instance.id))
            self.assertEqual(f.getvalue().strip(), instance_str)

        with patch('sys.stdout', new=StringIO()) as f:
            instance.new_att = "new_val"
            HBNBCommand().onecmd(f'show BaseModel {instance.id}')
            res = (
                f"[{instance.__class__.__name__}] "
                + f"({instance.id}) {instance.__dict__}")
            self.assertEqual(f.getvalue().strip(), res)

    def test_destroy_no_arg(self):
        """test_destroy_no_arg
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_destroy_wrong_model(self):
        """test_destroy_wrong_model
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy UnknownModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_correct_model_no_id(self):
        """test_destroy_correct_model_no_id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_correct_model_wrong_id(self):
        """test_destroy_correct_model_wrong_id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123-123-13")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all_no_arg(self):
        """test_all_no_arg
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_all_wrong_model(self):
        """test_all_wrong_model
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all UnknownModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")


if __name__ == "__main__":
    unittest.main()
