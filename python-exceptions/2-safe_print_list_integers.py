#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for index in range(x):
        try:
            if isinstance(my_list[index], int)
                print("{:d}".format(my_list[index]), end="")
                counter += 1
        except IndexError:
            raise
    print()
    return counter
