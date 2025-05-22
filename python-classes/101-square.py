#!/usr/bin/python3
"""
    This module defines a Square class.
"""
custom_type_error = TypeError("position must be a tuple of 2\
positive integers")


def sum_tuple(tuple_: tuple) -> int:
    listed_tuple = list(tuple_)
    count = 0
    for each in listed_tuple:
        count += each
    return count


class Square:
    """
        Represents a square with a given size.
        Attributes:
            __size (int): The size of the square's side. Must be >= 0.
    """
    SQUARE_SYMBOL = "#"
    squares_list = []

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
        Initializes a Square instance.
            Args:
                size (int): The size of the square. Must be an integer >= 0.
                position (tuple): A square coordinate. \
                    Must be an int tuple !negative
            Raises:
                TypeError: If size is not int, position not positive \
                    int tuple or length != 2
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
            # Use this code if coordinates are used to replace a specific
            # character from the square instead of using them for Off-setting
            # the square.
            # if (item > size -1):
            #  position = (0, 0)
            #  print(f"Warning: Out of bounds position, Square Size:\
            #   {size}. Position Reset.")
        self.size = size
        self.position = position  # uses the setter
        self.squares_list.append(self)

    def __str__(self):
        if (self.size == 0):
            return
        return f"{self.my_print()}"

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
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> int:
        """
            Retrieves a Square's coordinates.
            Returns: or not -> ?
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
        if (self.size == 0):
            print("")
        else:
            for item in range(self.position[1]):
                print()
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for column in range(self.size):
                    print(Square.SQUARE_SYMBOL, end="")
                print()

# new_square1 = Square(4, (3, 3))
# new_square1.my_print()
# print("Other Square:")
# new_square2 = Square(6, (3, 6))
# print(new_square.position)
# new_square.position = (1, 2)
# print("------- IULIUS CAESAR -------")
# print(new_square.position)
# new_square2.my_print()

# print(f"Square Print inside class: {new_square2}")
