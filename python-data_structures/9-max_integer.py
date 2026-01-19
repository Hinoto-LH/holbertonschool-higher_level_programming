#!/usr/bin/python3
def max_integer(my_list=[]):
    val_max = 0
    if my_list == []:
        return None
    else:
        for index in my_list:
            if index > val_max:
                val_max = index
        return val_max
