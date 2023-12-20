#!/usr/bin/python3

"""
Square Module
This module defines the Square class.
"""


class Square:
    """
    Square class
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer or position is not a tuple
            of 2 positive integers.
            ValueError: If size is less than 0 or position contains
            non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Args:
            value (int): The value to set as the size.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.
        Args:
            value (tuple): The value to set as the position.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) !=
        2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        If size is equal to 0, print an empty line.
        Position should be used by using space.
        Don’t fill lines with spaces when position[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
