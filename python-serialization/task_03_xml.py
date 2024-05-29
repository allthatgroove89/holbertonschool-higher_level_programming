#!/usr/bin/env python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    def convert_value(value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                if value.lower() in ['true', 'false']:
                    return value.lower() == 'true'
                return value

    dictionary = {}
    for child in root:
        dictionary[child.tag] = convert_value(child.text)
    return dictionary
