#!/usr/bin/python3
"""
Defines a Rectangle class.
"""

RECTANGLE_SYMBOL = "#"


class Rectangle:
    """
    Defines a rectangle, with its width and height (Must be int)
    """
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int = 0):
        if isinstance(width, int) and width >= 0:
            self.__width = width
        elif isinstance(width, int) and width < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int = 0):
        if isinstance(height, int) and height >= 0:
            self.__height = height
        elif isinstance(height, int) and height < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self) -> int:
        return self.width * self.height

    def perimeter(self) -> int:
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        rectangle_string = ""
        if self.width == 0 or self.height == 0:
            return rectangle_string
        else:
            for row in range(self.height):
                rectangle_string += RECTANGLE_SYMBOL * self.width + '\n'
        return rectangle_string

rect1 = Rectangle(3, 5)
print(rect1)
