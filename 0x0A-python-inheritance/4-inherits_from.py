#!/usr/bin/python3
"""This is a module with method it inherits_from"""


def inherits_from(obj, a_class):
    """This is a Method that return True if an object is an instance of a class
    that is inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
