#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialize Rectangle"""

    def __init__(self, width, height):

        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.___width = width
        self.__height = height

    def area(self):
        """Calculates area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
