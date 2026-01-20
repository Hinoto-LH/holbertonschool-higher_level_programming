#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(set(my_list))
    return result
# Dans un set, chaque élément doit être unique et immuable , c'est-à- dire \
# qu'il ne peut pas être modifié, on peut y stocker des nombre, des tuples,
# mais pas de listes ni de dico
