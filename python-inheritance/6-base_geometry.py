#!/usr/bin/python3
"""
Empty class
"""


class BaseGeometry:
    """Empty BaseGeometry class"""
    pass

    def area(self):
        """Raise exception if the area
        of a shape is not implemented"""
        raise Exception("area() is not implemented")
