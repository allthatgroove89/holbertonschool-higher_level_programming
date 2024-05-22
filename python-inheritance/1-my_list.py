#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):  # MyList class inherits list
    def print_sorted(self):
        """This is a public instance method."""
        print(sorted(self))
