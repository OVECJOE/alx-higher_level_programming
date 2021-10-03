#!/usr/bin/python3
"""A module that contains a linked list implementation"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the data and a pointer to the next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the value of the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node of the linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets a pointer to the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a Singly Linked List"""

    def __init__(self):
        """Initialize the head node"""
        self.__head = None

    def __str__(self):
        """Output format for the linked list"""
        current, values = self.__head, []
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new node into the list and sorts the list"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new.next_node, current.next_node = current.next_node, new
