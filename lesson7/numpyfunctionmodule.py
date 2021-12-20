import numpy as np


def matrix_function(x, y):
    rand_matrix = np.random.random((x, y))
    print(rand_matrix)
    print(rand_matrix.transpose())
    return rand_matrix



