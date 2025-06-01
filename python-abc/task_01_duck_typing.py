#!/usr/bin/python3
"""
Module that defines an abstract class for shapes and use duck typing to handle
objects of different shapes uniformly.
"""
import abc
import math


class Shape(abc.ABC):
    """
    Abstract class for implementid geometric shapes, with the inclusion of
    finding its area and perimeter.
    """
    @abc.abstractmethod
    def area(self) -> float:
        pass

    @abc.abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    """
    Implements a circle and methods to find its area and perimeter
    using the math library
    Arguments:
        (int, float) radius: the circle's radius
    """
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float:
        return (math.pi * (self.radius ** 2))

    def perimeter(self) -> float:
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    Implements a rectangle and methods to find its area and perimeter
    using the math library
    Arguments:
        (int, float) width: the rectangle's width.
        (int, float) height: the rectangle's height.
    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> float:
        return (self.width * self.height)

    def perimeter(self) -> float:
        return 2 * (self.height + self.width)


def shape_info(geometric_object):
    print(f"Area: {geometric_object.area():.3f}")
    print(f"Perimeter: {geometric_object.perimeter():.3f}")

# circle1 = Circle(12)
# shape_info(circle1)
# rectangle1 = Circle(13)
# shape_info(rectangle1)
