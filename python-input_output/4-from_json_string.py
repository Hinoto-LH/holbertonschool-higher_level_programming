#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string
    """

    # Convert the JSON string into a Python data structure
    return json.loads(my_str)
