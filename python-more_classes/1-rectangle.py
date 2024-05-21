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
