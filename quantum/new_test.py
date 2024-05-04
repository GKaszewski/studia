import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.integrate import quad


# Define the expression as a function
def expression(n, x):
    # Define the Hermite polynomial squared
    hermite_squared = hermite(n)(x) ** 2

    # Define the integrand as a lambda function
    integrand = lambda x: np.exp(-x ** 2) * hermite_squared

    # Calculate the integral
    integral, _ = quad(integrand, -np.inf, np.inf)

    # Calculate the term in the sum
    term = 1 / (np.sqrt(np.pi) * (2 ** (n) * np.math.factorial(n))) * integral

    return term


# Create an array of n values
n_values = np.arange(10)

# Create an array of x values for plotting
x_values = np.linspace(-5, 5, 1000)

# Calculate the expression for each n and x
result = np.zeros((len(n_values), len(x_values)))
for i, n in enumerate(n_values):
    result[i] = expression(n, x_values)

# Plot the results
plt.figure(figsize=(10, 6))
for i, n in enumerate(n_values):
    plt.plot(x_values, result[i], label=f'n={n}')
plt.title('Visualization of the Expression')
plt.xlabel('x')
plt.ylabel('Expression Value')
plt.legend()
plt.grid(True)
plt.show()
