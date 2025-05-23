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
        try:
            width = int(width)
        except (TypeError, ValueError):
            raise TypeError("width must be an integer")
        # if isinstance(width, int) and width >= 0:
        #     self.__width = width
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int = 0):
        try:
            height = int(height)
        except (TypeError, ValueError):
            raise TypeError("height must be an integer")
        # if isinstance(height, int) and height >= 0:
        #     self.__width = height
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

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
                rectangle_string += RECTANGLE_SYMBOL * self.width
                if row < self.height - 1:
                    rectangle_string += '\n'
        return rectangle_string

    def __repr__(self):
        return f"Rectangle{self.width, self.height}"

# rect1 = Rectangle(3, 3)
# print(rect1)
# print(repr(rect1))
# myrectangle = Rectangle(2, 4)
# print(str(rect1))
