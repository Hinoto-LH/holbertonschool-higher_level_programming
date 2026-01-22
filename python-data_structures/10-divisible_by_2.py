#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_in = []
    for element in my_list:
        if element % 2 == 0:
            div_in.append(True)
        else:
            div_in.append(False)
    return div_in
# Dans une liste nous pouvons ajouter tout type
