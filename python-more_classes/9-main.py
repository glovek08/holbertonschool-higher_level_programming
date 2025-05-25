#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

# my_square = Rectangle.square(5)
# print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
# print(my_square)
try:
    my_square1 = Rectangle.square("12")
    print("{} / {}".format(my_square1.width, my_square1.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
