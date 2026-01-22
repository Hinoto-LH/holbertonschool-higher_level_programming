#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        val_max = my_list[0]
        for index in my_list:
            if index > val_max:
                val_max = index
        return val_max
