import numpy as np

a = [int(x) for x in np.linspace(1, 20, 10)]
b = np.linspace(0, 1, 10)

print(f'a = {a}, b = {b}')


def multiply(vec_1, vec_2):
    return vec_1 * vec_2


print(f'a * b = {multiply(a, b)}')


def scalar_multiply(vec, scalar):
    return [x * scalar for x in vec]


print(f'a * 2 = {scalar_multiply(a, 2)}')


def matrix_4x4():
    return np.random.randint(1, 100, (4, 4))


def diagonal_of_matrix(mat):
    return np.diag(mat)


def transpose_of_matrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


w = matrix_4x4()
diag = diagonal_of_matrix(w)
print(f'w = \n{w},\n diag = {diag}')
transposed = transpose_of_matrix(w)
print(f'transposed =\n {np.array(transposed)}')
