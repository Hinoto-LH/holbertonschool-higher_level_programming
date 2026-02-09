#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """

    # Convert the Python object to a JSON formatted string
    return json.dumps(my_obj)
