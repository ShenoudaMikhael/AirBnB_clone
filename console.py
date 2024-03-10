#!/usr/bin/python3
"""Console entry Module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """AirBnb shell"""

    # intro = "Welcome to the airbnb shell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    file = None

    class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def default(self, line):
        """defualt action"""
        action_list = {
            "all": self.do_all,
            "count": self.do_count,
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        try:
            string = eval(line)
            action_list[string[0]](
                string[1].strip(), string[2] if len(string) == 3 else None
            )
        except Exception as e:
            print(e)

    def do_count(self, arg, other=None):
        """Get model count"""
        q = storage.all()

        qu = {k: q[k] for k in q if k.split(".")[0] == arg}
        print(len(qu.keys()))

    def do_create(self, arg, other=None):
        """Creates a new instance of class <arg>"""

        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in self.class_list:
            print("** class doesn't exist **")
            return

        new_instance = self.class_list[arg.split(" ")[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg, other=None):
        """Prints the string representation of an instance"""
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

    def do_destroy(self, arg, other=None):
        """Deletes an instance based on the class name and id"""
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
            storage.destroy("{}.{}".format(inputs[0], inputs[1]))
        else:
            print("** no instance found **")

    def do_all(self, arg, other=None):
        """Prints all string representation of all instances."""
        if len(arg) > 0 and arg not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        qu = storage.all()
        if arg:
            qu = {item: qu[item] for item in qu.keys() if item.split(".")[0] == arg}
        print([str(qu[model]) for model in qu])

    def do_update(self, arg, my_dict=None):
        """Updates an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) > 0 and arg.split(" ")[0] not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        inputs = arg.split(" ")
        if len(inputs) < 2:
            print("** instance id missing **")
            return
        all_data = storage.all()
        if "{}.{}".format(inputs[0], inputs[1]) in all_data:
            if len(inputs) < 3 and my_dict is None:
                print("** attribute name missing **")
                return
            if len(inputs) < 4 and my_dict is None:
                print("** value missing **")
                return

            current_instance = storage.all()["{}.{}".format(inputs[0], inputs[1])]
            # check for dict
            if my_dict is not None:
                for k in my_dict:
                    current_instance.update_atts(att=k, val=my_dict[k])
            else:
                current_instance.update_atts(att=inputs[2], val=inputs[3])
            storage.save()
        else:
            print("** no instance found **")
        # User.update("b2b20961-e142-4aa5-a4fa-c129ed40567c",{"naem":"asdasd","name":"asdasd"}

    # ----- basic shell commands -----
    def do_print_args(self, arg):
        """echo args to shell"""
        print(*parse(arg))

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """nothing on empty line"""
        pass


def parse(arg):
    "Convert a series of zero or more strings to an argument tuple"
    return tuple(map(str, arg.split()))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
