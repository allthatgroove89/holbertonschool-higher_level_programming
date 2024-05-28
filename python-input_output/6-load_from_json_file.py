#!/usr/bin/python3
"""This module contains a function that creates a
Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Reads a JSON file and returns a Python object."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
