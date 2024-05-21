#!/usr/bin/python3
"""
This module defines the previous empty Rectangle class

It defines its width and height
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    """Instance attribute to retrieve value"""
    @property
    def width(self):
        return self._Rectangle__width
    """Property setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
    """Instance attribute"""
    @property
    def height(self):
        return self._Rectangle__height
    """Property setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
