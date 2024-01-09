#!/usr/bin/python3
"""This is a module with method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """This is a Method that return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
