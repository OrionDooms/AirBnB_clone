#!/usr/bin/python3
"""Defines HBNBCommand command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand class"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program"""
        return True

    do_EOF = do_quit
    """EOF to exit the program"""

    def emptyline(self):
        """ENTER shouldn’t execute anything"""
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
