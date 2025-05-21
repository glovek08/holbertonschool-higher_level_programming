#!/usr/bin/python3
"""
    This module defines a Square class.
"""


custom_type_error = TypeError("position must be a tuple of 2 positive integers")
class Square:
    """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square's side. Must be >= 0.
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
            Initializes a Square instance.

            Args:
                size (int): The size of the square. Must be an integer >= 0.
                position (tuple): A square coordinate. Must be an int tuple !negative

            Raises:
                TypeError: If size is not int, position not positive int tuple or length != 2
                ValueError: If size is less than 0.
        """
        if not (isinstance(position, tuple)):
            raise custom_type_error
        elif (len(position) != 2):
            raise custom_type_error
        for item in position:
            if not isinstance(item, int):
                raise custom_type_error
            elif (item < 0):
                raise custom_type_error

        self.size = size
        self.__position = position #use the setter?

    @property
    def size(self) -> int:
        """
            Retrieves the size of the square.

            Returns:
                int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
            Sets the size of the square.

            Args:
                value (int): The new size value.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> int:
        """
            Retrieves the a coordinate of the square.

            Returns:
                int: The position at the given coordinate.
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
            Sets the
        """
        for item in value:
            if not (isinstance(item, int)):
                raise custom_type_error
        self.__position = value

    def area(self) -> int:
        """
            Calculates the area of the square.

            Returns:
                int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
            Prints the square object.
            If size = 0, it prints nothing.
        """
        square_symbol = "#"
        if (self.size == 0):
            print()
        else:
            for row in range(self.size):
                print(square_symbol * self.size)

# new_square = Square(12, (1, 5))
# new_square.my_print()
# print(new_square.position)
# new_square.position = (1, 2)
# print("-------------")
# print(new_square.position)
