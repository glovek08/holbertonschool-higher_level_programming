def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
        Arguments:
        obj = given object
        a_class = the class that should be the exact type of @obj
    Return:
        True: if @obj is kind of an instance of @a_class
        False: otherwise

    Examples:
    >>> is_kind_of_class(1, int)
    True
    >>> is_kind_of_class(1, float)
    False
    >>> is_kind_of_class(1, object)
    True
    >>> is_kind_of_class([1, 2], list)
    True
    >>> is_kind_of_class([1, 2], object)
    True
    >>> class MyClass:
    ...     pass
    >>> class MySubClass(MyClass):
    ...     pass
    >>> obj1 = MyClass()
    >>> obj2 = MySubClass()
    >>> is_kind_of_class(obj1, MyClass)
    True
    >>> is_kind_of_class(obj2, MyClass)
    True
    >>> is_kind_of_class(obj1, MySubClass)
    False
    >>> is_kind_of_class(None, type(None))
    True
    >>> is_kind_of_class(True, bool)
    True
    >>> is_kind_of_class(True, int)
    True
    >>> is_kind_of_class("hello", str)
    True
    >>> is_kind_of_class("hello", object)
    True
    """
    return True if isinstance(obj, a_class) else False