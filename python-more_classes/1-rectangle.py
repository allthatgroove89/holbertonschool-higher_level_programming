#!/usr/bin/python3
"""
This module defines the previous empty Rectangle class

It defines its width and height
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    """Instance attribute to retrieve value"""
    @property
    def width(self):
        return self._width
    """Property setter"""
    @width.setter
    def width(self, value):
        self._width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
    """Instance attribute"""
    @property
    def height(self):
        return self._height
    """Property setter"""
    @height.setter
    def height(self, value):
        self._height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
