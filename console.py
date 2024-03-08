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

    intro = "Welcome to the airbnb shell. Type help or ? to list commands.\n"
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
           
            "multi-argued":
                {
                    "update": self.do_update
                }

        }
        try:
            
            string = eval(line)
            action_list[string[0]](string[1].strip())
            # string2 = string.split(" ")
            # model_name, method_name, args = string2
            # if method_name in action_list["non-argued"]:
            #     action_list["non-argued"][method_name]("{} {}".format(model_name, args))
            #     return
        except Exception as e:
            print(e)
        # parts = line.split(".")
        # if len(parts) >= 2:
        #     model_name, method_name = parts
        #     if model_name not in self.class_list:
        #         return
        #     if method_name in action_list["non-argued"]:
        #         action_list["non-argued"][method_name](model_name)
        #         return
        #     argued = method_name.split('(')
        #     if len(argued) == 2:
        #         if argued[0] in action_list["argued"]:
        #             arg = argued[1][1:-2]
        #             print(arg)
        #             print(argued)
        #             action_list["argued"][argued[0]]("{} {}".format(model_name, arg))
        #     # #  User.show()   return

    def do_count(self, arg):
        """Get model count"""
        q = storage.all()
        
        # qu = {k: q[k] for k in q if k.split(".")[0] == arg}
        print(len(q.keys()))

    def do_create(self, arg):
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

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name and"""
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

    def do_destroy(self, arg):
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

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        if len(arg) > 0 and arg not in self.class_list.keys():
            print("** class doesn't exist **")
            return
        qu = storage.all()
        if arg:
            qu = {item: qu[item] for item in qu.keys() if item.split('.')[0] == arg}
        print([str(qu[model]) for model in qu])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)."""
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
        inputs = arg.split(" ")
        all_data = storage.all()
        if "{}.{}".format(inputs[0], inputs[1]) in all_data:
            if len(inputs) < 3:
                print("** attribute name missing **")
                return
            if len(inputs) < 4:
                print("** value missing **")
                return

            current_instance = storage.all()["{}.{}".format(inputs[0], inputs[1])]
            current_instance.update(inputs[2], inputs[3])
            storage.save()
        else:
            print("** no instance found **")

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
