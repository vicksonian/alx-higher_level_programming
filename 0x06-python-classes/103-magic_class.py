#!/usr/bin/python3

"""
MagicClass Module
This module defines the MagicClass class.
"""

import math


class MagicClass:
    """
    MagicClass class
    Represents a class with an area and circumference calculation.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.
        Args:
            radius: The radius of the MagicClass instance. Defaults to 0.
        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the MagicClass instance.
        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the MagicClass instance.
        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius

        if __name__ == "__main__":
            # Example usage:
            magic_instance = MagicClass(5)
            print("Area:", magic_instance.area())
            print("Circumference:", magic_instance.circumference())
