#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    for index in range(len(new_list)):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list
