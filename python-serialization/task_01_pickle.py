#!/usr/bin/env python3

import pickle


class CustomObject:
    def __init__(self, Name, age, is_student):
        self.Name = "John"
        self.age = 25
        self.is_student = True

    def __str__(self):
        return f"CustomObject: {self.Name}, {self.age}, {self.is_student}"

    def __repr__(self):
        return f"CustomObject: {self.Name}, {self.age} {self.is_student}"

    def display(self):
        print(f"Name: {self.Name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as ouput_file:
            pickle.dump(self, ouput_file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as input_file:
            pickle.load(cls, filename)
