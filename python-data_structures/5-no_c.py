#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for car in my_string:
        if car != "c" and car != "C":
            new_string += car
    return new_string
