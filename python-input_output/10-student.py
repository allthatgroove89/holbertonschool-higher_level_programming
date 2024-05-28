#!/usr/bin/python3
"""
Initializes a Student class.
"""


class Student:
    """
    Initializes a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for IstAttrs in attrs:
                if IstAttrs in self.__dict__.keys():
                    new_dict[IstAttrs] = self.__dict__[IstAttrs]
            return new_dict
