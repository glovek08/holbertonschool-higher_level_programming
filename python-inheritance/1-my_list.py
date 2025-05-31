#!/usr/bin/python3
"""
Module that defines a MyList class that inherites from the list master object.
"""


class MyList(list):
    """
    Class that defines a public method for printing lists.
    """
    def print_sorted(self):
        """
        Public method that prints a given list of
            integers in sorted ascending order.
        """
        print(sorted(self))

# list1 = MyList()
# list1.append(12)
# list1.append(4)
# list1.append(6)
# list1.print_sorted()
