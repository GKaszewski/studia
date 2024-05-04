import numpy as np


def add_matrices(a, b):
    return a + b


def subs_matrices(a, b):
    return a - b


def dot_product(a, b):
    return a * b


def sum_all_elements_in_column(mat, col):
    return np.sum(mat[:, col])


def sum_all_elements_in_row(mat, row):
    return np.sum(mat[row, :])


def sum_all_columns(mat):
    return np.sum(mat, axis=0)


def sum_all_rows(mat):
    return np.sum(mat, axis=1)


def inverse_matrix(mat):
    return np.linalg.inv(mat)


a = np.array([[1, 2], [4, 5]])
b = np.array([[10, 12], [14, 15]])

add = add_matrices(a, b)
sub = subs_matrices(a, b)
dot = dot_product(a, b)
sum_cols = sum_all_columns(a)
sum_rows = sum_all_rows(a)
inverse = inverse_matrix(a)

print(
    f'a = \n{a},\n b = \n{b},\n add = \n{add},\n sub = \n{sub},\n dot = \n{dot},\n sum_cols = \n{sum_cols},\n sum_rows = \n{sum_rows},\n inverse = \n{inverse}')
