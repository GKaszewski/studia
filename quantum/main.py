import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special, integrate


def generate_plots(start, end):
    x = np.linspace(-3, 3, 400)
    for i in range(start, end):
        func = special.hermite(i)
        plt.plot(x, func(x))
        plt.xlabel('$x$')
        plt.ylabel('$H_0(x)$')
        plt.title(f'Hermite polynomial {i}')
        plt.grid()
        plt.savefig(f'plots/hermite_{i}.png')
        plt.show()


# generate_plots(0, 11)


def custom_integral(n, x_arg=0):
    def integrand(x):
        hn = special.hermite(n)(x)
        return np.exp(-x ** 2) * hn ** 2

    integral = integrate.quad(integrand, -100, 100)[0]
    pre_factor = 1 / (math.sqrt(math.pi) * (2 ** n * math.factorial(n)))
    return pre_factor * integrand(x_arg)


# def get_matrix_old(n):
#     matrix = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             matrix[i, j] = np.sqrt(custom_integral(i + j))
#             print(f'Calculated matrix element ({i}, {j})')
#     return matrix


def get_matrix(n):
    n_values = range(n)
    matrix = np.zeros((len(n_values), len(n_values)))

    # Calculate the values and fill the matrix
    for i, n in enumerate(n_values):
        for j, m in enumerate(n_values):
            def integrand(x):
                hn = special.hermite(n)(x)
                hm = special.hermite(m)(x)
                return np.exp(-x ** 2) * hn * hm

            integral = integrate.quad(integrand, -np.inf, np.inf, epsabs=1e-6, epsrel=1e-6)[0]
            pre_factor_n = 1 / (math.sqrt(math.pi) * (2 ** n * math.factorial(n)))
            pre_factor_m = 1 / (math.sqrt(math.pi) * (2 ** m * math.factorial(m)))

            matrix[i, j] = pre_factor_n * pre_factor_m * integral
            print(f'Calculated matrix element ({i}, {j})')
    return matrix


# results = [custom_integral(n) for n in range(0, 11)]
# print(results)

# plt.matshow(get_matrix_old(10))
# plt.colorbar()
# plt.savefig('plots/matrix.png')
# plt.show()

values = [custom_integral(10, x) for x in np.linspace(-3, 3, 200)]
plt.plot(np.linspace(-3, 3, 200), values)
plt.xlabel('$x$')
plt.ylabel('$H_{10}(x)$')
plt.title('Hermite polynomial 10')
plt.grid()
plt.savefig('plots/hermite_11.png')
plt.show()