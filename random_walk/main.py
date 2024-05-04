import matplotlib.pyplot as plt
import numpy as np
import random

def random_walk(n_steps):
    x, y = [0], [0]

    for _ in range(n_steps):
        angle = np.random.uniform(0, 2 * np.pi)
        step_x = np.random.choice([-1, 1])
        step_y = np.random.choice([-1, 1])

        step_x = step_x * np.cos(angle)
        step_y = step_y * np.sin(angle)

        x.append(x[-1] + step_x)
        y.append(y[-1] + step_y)

    return x, y


def random_walk_normal(n_steps, mean=0, std=1):
    x, y = [0], [0]

    for _ in range(n_steps):
        step_x, step_y = calculate_step_normal(mean, std)

        x.append(x[-1] + step_x)
        y.append(y[-1] + step_y)

    return x, y


def random_walk_each_step_different_distribution(n_steps, mean=0, std=1):
    x, y = [0], [0]

    for i in range(n_steps):
        should_use_normal = np.random.choice([True, False])
        if should_use_normal:
            step_x, step_y = calculate_step_normal(mean, std)
        else:
            step_x = np.random.choice([-1, 1])
            step_y = np.random.choice([-1, 1])

        x.append(x[-1] + step_x)
        y.append(y[-1] + step_y)

    return x, y


def calculate_step_square():
    # Choose a direction: 0 - right, 1 - up, 2 - left, 3 - down
    direction = random.choice([0, 1, 2, 3])
    # Move one step in the chosen direction
    if direction == 0:  # right
        return 1, 0
    elif direction == 1:  # up
        return 0, 1
    elif direction == 2:  # left
        return -1, 0
    elif direction == 3:  # down
        return 0, -1


def random_walk_square(n_steps):
    x, y = [0], [0]

    for _ in range(n_steps):
        step_x, step_y = calculate_step_square()

        x.append(x[-1] + step_x)
        y.append(y[-1] + step_y)

    return x, y


def calculate_step_normal(mean, std):
    angle = np.random.uniform(0, 2 * np.pi)
    step_x = np.random.normal(mean, std)
    step_y = np.random.normal(mean, std)
    step_x = step_x * np.cos(angle)
    step_y = step_y * np.sin(angle)
    return step_x, step_y


def calculate_frequency(n_steps, n_trials, mean=0, std=1, normal=False):
    frequencies_x, frequencies_y = [0], [0]
    for _ in range(n_trials):
        x, y = random_walk_normal(n_steps, mean, std) if normal else random_walk(n_steps)
        end_x, end_y = x[-1], y[-1]
        frequencies_x.append(frequencies_x)
        frequencies_y.append(frequencies_y)
    return frequencies_x, frequencies_y


def plot_histogram_frequency(x, y):
    plt.figure(figsize=(10, 10))
    plt.hist2d(x, y, bins=100, cmap='Blues')
    plt.title('2D Random Walk')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()


def plot_histogram(x, y):
    plt.figure(figsize=(10, 10))
    plt.hist2d(x, y, bins=100, cmap='Blues')
    plt.title('2D Random Walk')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()


def plot_walk(x, y):
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, '-o', markersize=2, linewidth=0.5)
    plt.title('2D Random Walk')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    x, y = random_walk(1000)
    plot_walk(x, y)
    # plot_histogram(x, y)
    freq_x, freq_y = calculate_frequency(1000, 100)

    x, y = random_walk_normal(1000)
    plot_walk(x, y)
    # plot_histogram(x, y)

    x, y = random_walk_each_step_different_distribution(1000)
    plot_walk(x, y)
    # plot_histogram(x, y)

    x, y = random_walk_square(1000)
    plot_walk(x, y)
    plot_histogram(x, y)
