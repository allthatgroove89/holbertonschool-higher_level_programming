#!/usr/bin/python3
"""
This module defines the previous empty Rectangle class

It defines its width and height
"""


class Rectangle:
    """Rectangle Module"""
    def __init__(self, width=0, height=0):
        self._Rectangle__height = height
        self._Rectangle__width = width

    def __str__(self):
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        return (('#' * self.__width + '\n') * self.__height)[:-1]

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
