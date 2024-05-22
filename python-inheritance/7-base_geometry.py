#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:

    def area(self):
        """Raise exception if the area
        of a shape is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value

        Parameters:
        name (str): The name of the value
        value (int): The value to validate

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
