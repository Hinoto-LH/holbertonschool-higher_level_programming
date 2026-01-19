#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print("{}".format(matrix[x][y]), end=" ")
        print()
# matrix = [[]]. x = nombre de tableaux dans matrix
# y = nombre d'element dans chaque x
