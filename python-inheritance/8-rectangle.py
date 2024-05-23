#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialize Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.___width = width
        self.integer_validator("width", height)
        self.__height = height
