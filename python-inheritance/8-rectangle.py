#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """Raise exception if the area
        of a shape is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate integer value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Initialize Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.___width = width
        self.integer_validator("width", height)
        self.__height = height
