#!/usr/bin/python3
"""
Rectangle class module.
Define Rectangle class.
"""


class Rectangle:
    """Define a rectangle.
    number_of_instances (int): the number of instances currently in the scope.
    print_symbol (default='#'): the symbol to print in string representation.
    width (int)(default=0): the width of the rectangle.
    height (int)(default=0): the height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the larger rectangle, or rect_1 if equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @property
    def width(self):
        """Define width property."""
        return self.__width

    @property
    def height(self):
        """Define height property."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        value (int): the new length of the width.
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        value (int): the new length of the height.
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return the area of the rectangle."""
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string of the Rectangle of print_symbol (default '#')"""
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    string += str(self.print_symbol)
                if col is not (self.__height - 1):
                    string += "\n"
            return string

    def __repr__(self):
        """Return a formatable callable string of the class instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
