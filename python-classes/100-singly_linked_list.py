#!/usr/bin/python3
"""
    This module contains a Node class to create a
    singly linked list.
"""

data_type_error = TypeError("data must be an integer")
node_type_error = TypeError("next_node must be a Node object")


class Node:
    """
        Class Node represents an individual node of a singly
        linked list.
    """

    def __init__(self, data: int = 0, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise data_type_error
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise node_type_error
        self.__next_node = value


class SinglyLinkedList:
    """
        Creates a singly linked list.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """
            Make the list printable - prints each node number on a line.
        """
        if self.__head is None:
            return ""

        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)

    def sorted_insert(self, value):
        """
            Insert a new Node into the correct sorted\
                position in the list (increasing order).
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
