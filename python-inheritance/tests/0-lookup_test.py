#!/usr/bin/python3
"""
In this module we define a Fucking class and a shit object.

>>> # Test class instantiation
>>> f = Fucking()
>>> isinstance(f, Fucking)
True

>>> # Test the pre-created shit object
>>> isinstance(shit, Fucking)
True

>>> # Test that Fucking class has no custom methods (just passes)
>>> custom_methods = [attr for attr in dir(Fucking) if not attr.startswith('_')]
>>> custom_methods
[]

>>> # Test lookup function with the shit object
>>> methods = lookup(shit)
>>> isinstance(methods, list)
True

>>> # Test that lookup returns standard object methods
>>> '__init__' in lookup(shit)
True
>>> '__class__' in lookup(shit)
True
>>> '__str__' in lookup(shit)
True

>>> # Test lookup with different object types
>>> lookup(42)  # doctest: +ELLIPSIS
['__abs__', '__add__', ..., 'real']

>>> lookup("hello")  # doctest: +ELLIPSIS
['__add__', '__class__', ..., 'zfill']

>>> # Test that lookup returns the same as dir()
>>> lookup(shit) == dir(shit)
True

>>> # Test empty class behavior
>>> f1 = Fucking()
>>> f2 = Fucking()
>>> f1 is not f2  # Different instances
True
>>> type(f1) == type(f2)  # Same type
True
"""

class Fucking:
    """
    Fucking class doesn't do shit
    
    >>> f = Fucking()
    >>> f.__class__.__name__
    'Fucking'
    
    >>> # Test that it's a basic empty class
    >>> hasattr(f, '__dict__')
    True
    """
    pass

shit = Fucking()

def lookup(obj) -> list:
    """
    Returns a list of all methods of a given object, up to the core.
    
    >>> # Test with basic objects
    >>> result = lookup(123)
    >>> isinstance(result, list)
    True
    >>> len(result) > 0
    True
    
    >>> # Test with string
    >>> methods = lookup("test")
    >>> 'upper' in methods
    True
    >>> 'lower' in methods
    True
    
    >>> # Test with list
    >>> list_methods = lookup([1, 2, 3])
    >>> 'append' in list_methods
    True
    >>> 'pop' in list_methods
    True
    
    >>> # Test with our custom object
    >>> shit_methods = lookup(shit)
    >>> '__init__' in shit_methods
    True
    >>> isinstance(shit_methods, list)
    True
    """
    return dir(obj)

# print(lookup(shit))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)