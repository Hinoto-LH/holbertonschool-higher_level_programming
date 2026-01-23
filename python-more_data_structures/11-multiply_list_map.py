#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    def multi(x):
        return x * number
    return list(map(multi, my_list))
