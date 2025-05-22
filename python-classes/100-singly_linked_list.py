#!usr/bin/python3
"""
    This module contains a Node class to create a
    singly linked list.
"""

data_type_error = TypeError("data must be an integer")
next_node_type_error = TypeError("next_node must be a Node object")


class Node():
    """
        Class Node represents an individual node of a singly
        linked list.
    """

    def __init__(self, data: int = 0, next_node: Node = "None"):
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        return self.__data

    @data.setter
    def data(self, value: int = 0):
        if (isinstance(value, int)):
            self.__data = value
        else:
            raise data_type_error

    @property
    def next_node(self) -> Node:
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise next_node_type_error


class SinglyLinkedList():
    """
        Class that creates a singly linked list.
    """

    def __init__(self):
        pass

    def sorted_insert(self, value: Node = None):
        linked_list.append(Node)
