#!/usr/bin/python3
"""
This module writes an Object to a text file
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
