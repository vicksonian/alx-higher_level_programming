#!/usr/bin/python3
"""Module with class MyList
"""


class MyList(list):
    """Class with method to print_sorted"""
    pass

    def print_sorted(self):
        """Method for sorted lists"""

        print(sorted(list(self)))
