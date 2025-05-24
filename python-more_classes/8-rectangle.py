#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Defines a rectangle, with its width and height (Must be int)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
                rectangle_string += str(self.print_symbol) * self.width
                if row < self.height - 1:
                    rectangle_string += '\n'
        return rectangle_string

    def __repr__(self):
        return f"Rectangle{self.width, self.height}"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area()
                else rect_2)

# rect1 = Rectangle(3, 3)
# rect2 = Rectangle(4, 3)
# print(f"rect1:\n{rect1}")
# print(f"rect1 repr: {repr(rect1)}")
# print(f"rect1 hash: {rect1.__hash__()}")
# print(f"rect1 str:\n{str(rect1)}")
# print('---- ALEA IACTA EST! ----')
# print(f"rect2:\n{rect2}")
# print(f"rect2 repr: {repr(rect2)}")
# print(f"rect2 hash: {rect2.__hash__()}")
# print(f"rect2 str:\n{str(rect2)}")
# print()
# print("Which one is bigger:")
# print(Rectangle.bigger_or_equal(rect1, rect2))
