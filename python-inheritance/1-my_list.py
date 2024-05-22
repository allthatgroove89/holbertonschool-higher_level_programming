#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):  # MyList class inherits list
    """MyList class"""
    def __init__(self):
        """Initialize Class"""
        super().__init__()

    def print_sorted(self):
        """This is a public instance method."""
        print(sorted(self))
