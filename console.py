#!/usr/bin/python3
"""Console entry Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """AirBnb shell"""

    intro = "Welcome to the airbnb shell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    file = None

    # ----- basic turtle commands -----
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
