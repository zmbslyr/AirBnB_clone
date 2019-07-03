#!/usr/bin/python3
"""Module that contains the console for HBNB"""


import cmd
import sys
import models
from shlex import split
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Interpret commands for HBNB"""

    def __init__(self, *args, **kwargs):
        """Initialization Method"""

        super().__init__(*args, **kwargs)
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the command line interpreter"""

        return True

    def do_EOF(self, line):
        """Exits the command line interpreter when EOF is reached"""

        return True

    def do_create(self, line):
        """Creates a new data instance and stores it"""

        if len(line) == 0:
            print("** class name missing **")
            return

        try:
            args = split(line)
            newObj = eval(args[0])()
            newObj.save()
            print(newObj.id)

        except:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroys an instance based on class name and ID"""

        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        clsName = args[0]
        clsId = args[1]
        storage = FileStorage()
        storage.reload()
        objDict = storage.all()

        try:
            eval(clsName)

        except NameError:
            print("** class doesn't exist **")
            return

        key = clsName + "." + clsId

        try:
            del objDict[key]

        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_update(self, line):
        """Updates an instance based on class name and ID"""

        storage = FileStorage()
        storage.reload()
        args = split(line)

        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        try:
            eval(args[0])

        except NameError:
            print("** class doesn't exist **")
            return

        key = args[0] + "." + args[1]
        objDict = storage.all()

        try:
            objVal = objDict[key]

        except KeyError:
            print("** no instance found **")
            return

        try:
            attrType = type(getattr(objVal, args[2]))
            args[3] = attrType(args[3])

        except AttributeError:
            pass

        setattr(objVal, args[2], args[3])
        objVal.save()

    def do_show(self, line):
        """Prints string representation of an instance"""

        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        objDict = storage.all()

        try:
            eval(args[0])

        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]

        try:
            value = objDict[key]
            print(value)

        except KeyError:
            print("** no instance found **")

    def do_count(self, line):
        """Counts number of instances"""

        objList = []
        storage = FileStorage()
        storage.reload
        objs = storage.all()

        try:
            if len(line) != 0:
                eval(line)

        except NameError:
            print("** class doesn't exist **")
            return

        for _, value in objs.items():
            if len(line) != 0:
                if type(value) is eval(line):
                    objList.append(value)
            else:
                objList.append(value)
        print(len(objList))

    def emptyline(self):
        """Do nothing if an empty line is typed"""

        return False

    def do_all(self, line):
        """Prints all data instances, filtered by class (optional)"""

        objList = []
        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            if len(line) != 0:
                eval(line)

        except NameError:
            print("** class doesn't exist **")
            return

        for _, value in objs.items():
            if len(line) != 0:
                if type(value) is eval(line):
                    objList.append(value)
            else:
                objList.append(value)
        for i in objList:
            print(i)

    def default(self, line):
        """Catches all methods that are not defined"""

        funcs = {"all": self.do_all,
                 "update": self.do_update,
                 "show": self.do_show,
                 "count": self.do_count,
                 "destroy": self.do_destroy}
        args = (line.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", "").split("."))

        try:
            cmds = args[0] + " " + args[2]
            func = funcs[args[1]]
            func(cmds)

        except:
            print("** unknown syntax:", args[0])

if __name__ == "__main__":
    """Entry point for the command line loop"""
    HBNBCommand().cmdloop()
