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

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size: The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            Union[int, float]: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Args:
            value: The value to set as the size.
        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            Union[int, float]: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equal comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
       Less than comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if less than, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if greater than, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison method based on the square area.
        Args:
            other: The other square to compare.
        Returns:
            bool: True if greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

        if __name__ == "__main__":
            s_5 = Square(5)
            s_6 = Square(6)

        if s_5 < s_6:
            print("Square 5 < Square 6")
        if s_5 <= s_6:
            print("Square 5 <= Square 6")
        if s_5 == s_6:
            print("Square 5 == Square 6")
        if s_5 != s_6:
            print("Square 5 != Square 6")
        if s_5 > s_6:
            print("Square 5 > Square 6")
        if s_5 >= s_6:
            print("Square 5 >= Square 6")
