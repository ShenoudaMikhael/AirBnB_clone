#!/usr/bin/python3
"""Console entry Module"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnb shell"""

    intro = "Welcome to the airbnb shell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    file = None

    class_list = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of class <arg>"""

        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        new_instance = self.class_list[arg.split(" ")[0]]()
        new_instance.save()

    def do_show(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg.split(" ")[0] not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        if len(arg.split(" ")) < 2:
            print("** instance id missing **")
            return
        inputs = arg.split(" ")
        if "{}.{}".format(inputs[0], inputs[1]) in storage.all().keys():
            print(storage.all()["{}.{}".format(inputs[0], inputs[1])])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        if len(arg) > 0 and arg not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        qu = storage.all()
        print([qu[model].__str__() for model in qu])
        # There is a mistake

    # ----- basic shell commands -----
    def do_print_args(self, arg):
        "echo args to shell"
        print(*parse(arg))

    def do_quit(self, arg):
        "Quit command to exit the program"
        exit()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True


def parse(arg):
    "Convert a series of zero or more strings to an argument tuple"
    return tuple(map(str, arg.split()))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
