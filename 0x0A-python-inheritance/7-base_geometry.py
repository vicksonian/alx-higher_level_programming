#!/usr/bin/python3
"""This is a module with the class BaseGeometry"""


class BaseGeometry:
    """This is a BaseGeometry class"""

    def area(self):
        """method for calculating area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This Method is for validating if a num is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
