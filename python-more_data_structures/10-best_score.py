#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        save_key = None
    else:
        max_value = None
        for key, value in a_dictionary.items():
            if max_value is None:
                save_key = key
                max_value = a_dictionary[key]
            if max_value < value:
                save_key = key
                max_value = value
    return save_key
