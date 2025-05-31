#!/usr/bin/python3
"""
Module that checks if an object is an instance of a
class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        but not an instance of a_class itself; False otherwise.

    Examples:
        >>> class MyBaseClass:
        ...     pass
        >>> class MyDerivedClass(MyBaseClass):
        ...     pass
        >>> class MyOtherClass:
        ...     pass

        >>> obj_base = MyBaseClass()
        >>> obj_derived = MyDerivedClass()
        >>> obj_other = MyOtherClass()
        >>> int_obj = 10
        >>> str_obj = "hello"

        # Test cases where it should return True
        >>> inherits_from(obj_derived, MyBaseClass)
        True
        >>> inherits_from(obj_derived, object) # All classes inherit from object
        True
        >>> inherits_from(int_obj, object)
        True
        >>> inherits_from(str_obj, object)
        True

        # Test cases where it should return False (obj is directly a_class)
        >>> inherits_from(obj_base, MyBaseClass)
        False
        >>> inherits_from(10, int)
        False
        >>> inherits_from("hello", str)
        False

        # Test cases where obj is not an instance of a_class or its subclass
        >>> inherits_from(obj_base, MyDerivedClass)
        False
        >>> inherits_from(obj_other, MyBaseClass)
        False
        >>> inherits_from(obj_derived, MyOtherClass)
        False
        >>> inherits_from(obj_base, object)
        True

        # Test with built-in types
        >>> inherits_from(True, bool)
        False
        >>> inherits_from(True, int) # True is an instance of int (bool inherits from int)
        True
        >>> inherits_from(5.0, float)
        False
        >>> inherits_from(5.0, object)
        True
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

if __name__ == "__main__":
    import doctest
    doctest.testmod()
