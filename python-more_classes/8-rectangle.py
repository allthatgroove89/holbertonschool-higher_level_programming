#!/usr/bin/python3
"""
This module defines the previous empty Rectangle class

It defines its width and height
"""


class Rectangle:
    """Rectangle Module"""
    number_of_instances = 0  # This is a class attribute
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self._Rectangle__height = height
        self._Rectangle__width = width
        Rectangle.number_of_instances += 1   # Increment the count when
        # a new instance is created

    def __str__(self):
        """ Prints a rectangle with # character"""
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        return ((str(self.print_symbol) * self._Rectangle__width + '\n') *
                self._Rectangle__height)[:-1]

    def __repr__(self):
        """String representation of the rectangle"""
        return (
            'Rectangle({:d}, {:d})'
            .format(self._Rectangle__width, self._Rectangle__height)
        )

    """Method property"""
    @property
    def width(self):
        return self._Rectangle__width

    """Property setter"""
    @width.setter
    def width(self, value):
        """sets the value of widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    """Method property"""
    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """Calculates the perimeter of the Rectangle"""
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return 0
        return 2 * (self._Rectangle__height + self._Rectangle__width)

    def __del__(self):
        """deletes class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the count
        # when an instance is deleted

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static Method that return biggest rectangle area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
