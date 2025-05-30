#!/usr/bin/python3
"""
Module that defines a MyList class that inherites from the list master object.

>>> # Test basic instantiation
>>> ml = MyList()
>>> isinstance(ml, MyList)
True
>>> isinstance(ml, list)
True

>>> # Test with initial data
>>> ml = MyList([3, 1, 4, 1, 5])
>>> len(ml)
5
>>> ml[0]
3

>>> # Test inheritance - should have all list methods
>>> ml = MyList([1, 2, 3])
>>> ml.append(4)
>>> ml
[1, 2, 3, 4]

>>> # Test list operations
>>> ml = MyList([1, 2])
>>> ml.extend([3, 4])
>>> ml
[1, 2, 3, 4]

>>> # Test slicing
>>> ml = MyList([1, 2, 3, 4, 5])
>>> ml[1:3]
[2, 3]

>>> # Test iteration
>>> ml = MyList([1, 2, 3])
>>> [x * 2 for x in ml]
[2, 4, 6]
"""

class MyList(list):
    """
    Class that defines a public method for printing lists.
    
    >>> # Test empty list
    >>> ml = MyList()
    >>> ml.print_sorted()
    []
    
    >>> # Test with integers
    >>> ml = MyList([3, 1, 4, 1, 5, 9, 2, 6])
    >>> ml.print_sorted()
    [1, 1, 2, 3, 4, 5, 6, 9]
    
    >>> # Test that original list is unchanged
    >>> ml = MyList([5, 2, 8, 1])
    >>> ml.print_sorted()
    [1, 2, 5, 8]
    >>> ml  # Original should be unchanged
    [5, 2, 8, 1]
    
    >>> # Test with negative numbers
    >>> ml = MyList([-3, -1, -4, -1, -5])
    >>> ml.print_sorted()
    [-5, -4, -3, -1, -1]
    
    >>> # Test with mixed positive and negative
    >>> ml = MyList([3, -1, 4, -2, 0])
    >>> ml.print_sorted()
    [-2, -1, 0, 3, 4]
    
    >>> # Test with single element
    >>> ml = MyList([42])
    >>> ml.print_sorted()
    [42]
    
    >>> # Test with duplicates
    >>> ml = MyList([5, 5, 5, 5])
    >>> ml.print_sorted()
    [5, 5, 5, 5]
    
    >>> # Test inheritance behavior
    >>> ml = MyList([1, 2, 3])
    >>> ml.append(0)
    >>> ml.print_sorted()
    [0, 1, 2, 3]
    
    >>> # Test that it works after list modifications
    >>> ml = MyList([10, 5])
    >>> ml.insert(1, 7)
    >>> ml.print_sorted()
    [5, 7, 10]
    
    >>> # Test with large numbers
    >>> ml = MyList([1000, 1, 999])
    >>> ml.print_sorted()
    [1, 999, 1000]
    """
    
    def print_sorted(self):
        """
        Public method that prints a given list of
        integers in sorted ascending order.
        
        >>> # Basic functionality test
        >>> ml = MyList([3, 1, 2])
        >>> ml.print_sorted()
        [1, 2, 3]
        
        >>> # Test with already sorted list
        >>> ml = MyList([1, 2, 3, 4])
        >>> ml.print_sorted()
        [1, 2, 3, 4]
        
        >>> # Test with reverse sorted list
        >>> ml = MyList([4, 3, 2, 1])
        >>> ml.print_sorted()
        [1, 2, 3, 4]
        
        >>> # Test that method doesn't return anything (returns None)
        >>> ml = MyList([1, 3, 2])
        >>> result = ml.print_sorted()
        [1, 2, 3]
        >>> result is None
        True
        """
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)