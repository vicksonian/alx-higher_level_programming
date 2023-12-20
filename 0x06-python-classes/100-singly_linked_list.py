#!/usr/bin/python3

"""
Singly Linked List Module
This module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    Node class
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.
        Args:
            data: The data to store in the node.
            next_node: The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.
        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.
        Args:
            value: The value to set as the data.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.
        Returns:
            The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.
        Args:
            value: The value to set as the next_node.
        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
        list (increasing order).
        Args:
            value: The value to insert.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string for printing.
        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
