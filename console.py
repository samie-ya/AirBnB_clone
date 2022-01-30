#!/usr/bin/python3


"""
entry point for command interpreter
"""


import cmd
import models.base_model
from models import storage
import shlex
import json


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    all_classes = ['BaseModel', 'User', 'Place', 'City', 'Amenity',
                   'Review', 'State']

    def default(self, line):
        """This function intercepts any unknown syntax"""
        line_args = line.split(".", 1)
        if (line[len(line) - 1] != ')' or len(line_args) != 2):
            print("*** Unknown syntax: {}".format(line))
            return
        class_name = line_args[0]
        command = line_args[1]
        function = command.split("(")
        if (len(function) != 2):
            print("*** Unknown syntax: {}".format(line))
            return
        function_name = function[0]
        argument = (function[1]).replace(")", "")
        present = 0
        for each_class in self.all_classes:
            if (class_name == each_class):
                present = 1
                break
        if (present == 0):
            print("*** Unknown syntax: {}".format(line))
            return
        if (function_name == 'all' and argument == ""):
            self.do_all(class_name)
        elif (function_name == 'show'):
            self.do_show(class_name + ' ' + argument)
        elif (function_name == 'destroy'):
            self.do_destroy(class_name + ' ' + argument)
        elif (function_name == 'count' and argument == ""):
            all_objects = storage.all()
            count = 0
            for each_key in all_objects:
                clas = (each_key.split('.'))[0]
                if (class_name == clas):
                    count += 1
            print(count)
        elif (function_name == 'update'):
            args = argument.split(' ', 1)
            if ((args[1])[0] == '{' and (args[1])[len(args[1]) - 1] == '}'):
                try:
                    args[1] = (args[1]).replace("'", '"')
                    dict_rep = json.loads(args[1])
                    object_id = args[0]
                    for each_key in dict_rep:
                        value = dict_rep[each_key]
                        argument = object_id + ' ' + each_key + ' ' + value
                        argument = argument.replace(',', '', 1)
                        self.do_update(class_name + ' ' + argument)
                except:
                    print("*** Unknown syntax: {}".format(line))
            else:
                argument = argument.replace(',', '')
                self.do_update(class_name + ' ' + argument)
        else:
            print("*** Unknown syntax: {}".format(line))

    def emptyline(self):
        """This function ignores an empty line input"""
        pass

    def do_quit(self, line):
        """
        This function exits the interpreter
        Usage:
                (hbnb) quit
        """
        return (True)

    def do_EOF(self, line):
        """
        This function exits the interpreter when EOF is reached
        Usage:
                (hbnb) exit
        """
        print()
        return (True)

    def do_create(self, class_name):
        """
        This function creates an instance of <class_name>,
        saves it to a json file and prints the <id> of the instance
        Usage:
                (hbnb) create <class_name>
        """
        if (class_name == ""):
            print("** class name missing **")
            return
        if (class_name == 'BaseModel'):
            class_instance = models.base_model.BaseModel()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'User'):
            class_instance = models.user.User()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'Place'):
            class_instance = models.place.Place()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'State'):
            class_instance = models.state.State()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'City'):
            class_instance = models.city.City()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'Amenity'):
            class_instance = models.amenity.Amenity()
            class_instance.save()
            print(class_instance.id)
        elif (class_name == 'Review'):
            class_instance = models.review.Review()
            class_instance.save()
            print(class_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, class_name_and_id):
        """
        This function prints the string representation of an object
        Usage:
                (hbnb) show <class_name> <object_id>
        """
        if (class_name_and_id == ""):
            print("** class name missing **")
            return
        args_list = class_name_and_id.split()
        if (len(args_list) == 1):
            print("** instance id missing **")
            return
        class_name = args_list[0]
        id_no = shlex.split(args_list[1])
        object_id = class_name + '.' + id_no[0]
        present = 0
        for each_class in self.all_classes:
            if (class_name == each_class):
                present = 1
                break
        if (present == 0):
            print("** class doesn't exist **")
            return
        else:
            all_objects = storage.all()
            found = 0
            for obj_key in all_objects:
                if (object_id == obj_key):
                    print(all_objects[obj_key])
                    found = 1
            if (found == 0):
                print("** no instance found **")

    def do_destroy(self, class_name_and_id):
        """
        This function destroys an instance of a class
        and updates the file storage
        Usage:
                (hbnb) destroy <class_name> <object_id>
        """
        if (class_name_and_id == ""):
            print("** class name missing **")
            return
        args_list = class_name_and_id.split()
        if (len(args_list) == 1):
            print("** instance id missing **")
            return
        class_name = args_list[0]
        id_no = shlex.split(args_list[1])
        object_id = class_name + '.' + id_no[0]
        present = 0
        for each_class in self.all_classes:
            if (class_name == each_class):
                present = 1
                break
        if (present == 0):
            print("** class doesn't exist **")
            return
        else:
            all_objects = storage.all()
            found = 0
            for obj_key in all_objects:
                if (object_id == obj_key):
                    all_objects.pop(object_id)
                    storage.save()
                    found = 1
                    break
            if (found == 0):
                print("** no instance found **")

    def do_all(self, class_name):
        """
        This function prints the string representation
        of every object/instance of BaseModel class
        Usage:
                (hbnb) all <class_name> OR all
        """
        all_objects = storage.all()
        present = 0
        for each_class in self.all_classes:
            if (each_class == class_name):
                present = 1
                break
        if (class_name == ""):
            for obj_key in all_objects:
                print(all_objects[obj_key])
            return
        elif (present == 1):
            for each_key in all_objects:
                name = each_key.split(".")
                if (name[0] == class_name):
                    print(all_objects[each_key])
        else:
            print("** class doesn't exist **")

    def do_update(self, class_name_id_attr_name_id):
        """
        This function updates an existing object with the given attributes
        Usage:
                (hbnb) update <class_name> <object_id> <attr_name> <attr_id>
        """
        if (class_name_id_attr_name_id == ""):
            print("** class name missing **")
            return
        all_args = shlex.split(class_name_id_attr_name_id)
        if (len(all_args) == 1):
            print("** instance id missing **")
            return
        if (len(all_args) == 2):
            print("** attribute name missing **")
            return
        if (len(all_args) == 3):
            print("** value missing **")
            return
        class_name = all_args[0]
        object_id = all_args[1]
        attr_name = all_args[2]
        attr_value = all_args[3]
        number = attr_value.split('.')
        if (len(number) == 2):
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        elif (attr_value.isdigit()):
            try:
                attr_value = int(attr_value)
            except ValueError:
                pass
        object_key = class_name + '.' + object_id
        present = 0
        for each_class in self.all_classes:
            if (class_name == each_class):
                present = 1
                break
        if (present == 0):
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        found = 0
        for obj_key in all_objects:
            if (object_key == obj_key):
                found = 1
                break
        if (found == 0):
            print("** no instance found **")
            return
        old_obj = all_objects[object_key]
        obj_dict = old_obj.__dict__
        obj_dict[attr_name] = attr_value
        old_obj.__dict__ = obj_dict
        old_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
