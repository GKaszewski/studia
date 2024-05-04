# alpha - minimized
# beta - minimized
# theta - fixed
import datetime

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# E(a1, b1) + E(a1, b2) + E(a2, b1) - E(a2, b2)
def local_state(alpha, sign):
    return [[(1 + pow(-1, sign) * np.cos(alpha)) / 2, (pow(-1, sign) * np.sin(alpha)) / 2],
            [(pow(-1, sign) * np.sin(alpha)) / 2, (1 - pow(-1, sign) * np.cos(alpha)) / 2]]


def local_a(alpha, sign):
    return np.outer(local_state(alpha, sign), np.identity(2))


def local_b(beta, sign):
    return np.outer(np.identity(2), local_state(beta, sign))


def local_ab(alpha, beta, sign1, sign2):
    return np.outer(local_state(alpha, sign1), local_state(beta, sign2))


def theta_state(theta):
    return [np.cos(theta), 0, 0, np.sin(theta)]


def prob_a(alpha, theta, sign):
    vec = theta_state(theta)
    return np.dot(vec, np.dot(local_a(alpha, sign), vec)) / 2


def prob_b(beta, theta, sign):
    vec = theta_state(theta)
    return np.dot(vec, np.dot(local_b(beta, sign), vec)) / 2


def prob_ab(alpha, beta, theta, sign1, sign2):
    vec = theta_state(theta)
    return np.dot(vec, np.dot(local_ab(alpha, beta, sign1, sign2), vec)) / 2


for i in range(2):
    for j in range(2):
        print(f'ProbAB({i}, {j}) = {prob_ab(0.628, 0.1345, np.pi / 3, i, j)}')
for i in range(2):
    print(f'ProbA({i}) = {prob_a(0, np.pi / 5, i)}')


def val(p0, p1, p2, p3):
    q = np.random.random()
    if q < p0:
        return [0, 0]
    if q < p0 + p1:
        return [0, 1]
    if q < 1 - p3:
        return [1, 0]
    return [1, 1]


def get_avg_val(p0, p1, p2, p3):
    vals = []
    for _ in range(1000000):
        v = 1 if val(p0, p1, p2, p3) in [[0, 0], [1, 1]] else -1
        vals.append(v)
    return np.mean(vals)


print(f'avg: {get_avg_val(0.1, 0.2, 0.3, 0.4)}')


def A(a, b):
    return local_state(a, b)


state = [1, 0, 0, 1] / np.sqrt(2)


def prob(alpha, beta, a, b):
    return np.dot(np.dot(state, np.kron(A(alpha, a), A(beta, b))), state)


# k = [prob(0.323, k1 * np.pi / 1000, 0, 1) for k1 in range(1000)]
# plt.plot(k)
# plt.show()


def experiment(params):
    alpha, beta = params
    p0 = prob(alpha, beta, 0, 0)
    p1 = prob(alpha, beta, 0, 1)
    p2 = prob(alpha, beta, 1, 0)
    p3 = prob(alpha, beta, 1, 1)
    return get_avg_val(p0, p1, p2, p3)


# Initial guess for alpha and beta
initial_guess = [np.pi / 4, 0.25]


# Perform the minimization
# result = minimize(experiment, initial_guess, method='Nelder-Mead')
# optimized_parameters = result.x
# minimum_value = result.fun
# print(f"Optimized Parameters: {optimized_parameters}")
# print(f"Minimum Value: {minimum_value}")

# Problem. Plot Bell's theorem for optimized parameters
# data = [experiment(optimized_parameters) for i in np.linspace(0, np.pi, 100)]
# print(f'data: {data}')
# plt.plot(data)
# plt.annotate(f'Optimized Parameters: {optimized_parameters}', xy=(0.0, 1), xycoords='axes fraction')
# plt.show()

def E(a, b):
    # Calculate the matrices for angles a and b
    matrix_a_plus = local_state(a, 1)
    matrix_a_minus = local_state(a, -1)
    matrix_b_plus = local_state(b, 1)
    matrix_b_minus = local_state(b, -1)

    # Calculate the expectation value
    expectation = 0
    for i in range(2):
        for j in range(2):
            expectation += matrix_a_plus[i][j] * matrix_b_plus[i][j]
            expectation -= matrix_a_plus[i][j] * matrix_b_minus[i][j]
            expectation -= matrix_a_minus[i][j] * matrix_b_plus[i][j]
            expectation += matrix_a_minus[i][j] * matrix_b_minus[i][j]

    return expectation


def objective(angles):
    a1, a2, b1, b2 = angles
    return E(a1, b1) + E(a1, b2) + E(a2, b1) - E(a2, b2)


initial_angles_list = [np.random.uniform(0, 2 * np.pi, 4) for _ in range(10)]

results = []
for initial_angles in initial_angles_list:
    result = minimize(objective, initial_angles, method='Nelder-Mead')
    results.append((result.x, result.fun))

# Finding the best result
best_result = min(results, key=lambda x: x[1])
print("Optimal angles:", best_result[0])
print("Minimum value:", best_result[1])
