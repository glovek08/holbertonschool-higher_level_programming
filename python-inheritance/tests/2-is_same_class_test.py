#!/usr/bin/python3
"""
Test file for is_same_class function
"""

# Import the function
is_same_class = __import__('2-is_same_class').is_same_class

# Test basic types
print("=== Basic Types ===")
a = 1
print(f"is_same_class(1, int): {is_same_class(a, int)}")  # True
print(f"is_same_class(1, float): {is_same_class(a, float)}")  # False
print(f"is_same_class(1, object): {is_same_class(a, object)}")  # False

# Test string
print("\n=== String ===")
b = "Hello"
print(f"is_same_class('Hello', str): {is_same_class(b, str)}")  # True
print(f"is_same_class('Hello', int): {is_same_class(b, int)}")  # False

# Test list
print("\n=== List ===")
c = [1, 2, 3]
print(f"is_same_class([1,2,3], list): {is_same_class(c, list)}")  # True
print(f"is_same_class([1,2,3], object): {is_same_class(c, object)}")  # False

# Test dict
print("\n=== Dictionary ===")
d = {'key': 'value'}
print(f"is_same_class({{'key': 'value'}}, dict): {is_same_class(d, dict)}")  # True
print(f"is_same_class({{'key': 'value'}}, list): {is_same_class(d, list)}")  # False

# Test None
print("\n=== None ===")
print(f"is_same_class(None, type(None)): {is_same_class(None, type(None))}")  # True
print(f"is_same_class(None, int): {is_same_class(None, int)}")  # False

# Test boolean (important edge case)
print("\n=== Boolean ===")
print(f"is_same_class(True, bool): {is_same_class(True, bool)}")  # True
print(f"is_same_class(True, int): {is_same_class(True, int)}")  # False (bool inherits from int)

# Test float
print("\n=== Float ===")
pi = 3.14
print(f"is_same_class(3.14, float): {is_same_class(pi, float)}")  # True
print(f"is_same_class(3.14, int): {is_same_class(pi, int)}")  # False

# Test custom classes
print("\n=== Custom Classes ===")
class MyClass:
    pass

obj = MyClass()
print(f"is_same_class(MyClass(), MyClass): {is_same_class(obj, MyClass)}")  # True
print(f"is_same_class(MyClass(), object): {is_same_class(obj, object)}")  # False

# Test inheritance (key distinction from isinstance)
print("\n=== Inheritance ===")
class Parent:
    pass

class Child(Parent):
    pass

child_obj = Child()
print(f"is_same_class(Child(), Child): {is_same_class(child_obj, Child)}")  # True
print(f"is_same_class(Child(), Parent): {is_same_class(child_obj, Parent)}")  # False
print(f"is_same_class(Child(), object): {is_same_class(child_obj, object)}")  # False

# Comparison with isinstance to show the difference
print("\n=== Comparison with isinstance ===")
print(f"isinstance(Child(), Child): {isinstance(child_obj, Child)}")  # True
print(f"isinstance(Child(), Parent): {isinstance(child_obj, Parent)}")  # True (different!)
print(f"isinstance(Child(), object): {isinstance(child_obj, object)}")  # True (different!)

print(f"is_same_class(Child(), Child): {is_same_class(child_obj, Child)}")  # True
print(f"is_same_class(Child(), Parent): {is_same_class(child_obj, Parent)}")  # False
print(f"is_same_class(Child(), object): {is_same_class(child_obj, object)}")  # False

print("\n=== All tests completed ===")