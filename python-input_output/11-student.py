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
            for IsAttrs in attrs:
                if IsAttrs in self.__dict__.keys():
                    new_dict[IsAttrs] = self.__dict__[IsAttrs]
            return new_dict

    def reload_from_json(self, json):
        """reload_from_json"""
        list_keys = list(json.keys())
        for j in list_keys:
            self.__dict__[j] = json.get(j)
