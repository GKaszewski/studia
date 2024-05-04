import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def normalize_data(data):
    ids = data.iloc[:, 0]
    normalized = (data.iloc[:, 1:] - data.iloc[:, 1:].mean()) / data.iloc[:, 1:].std()
    return pd.concat([ids, normalized], axis=1)


def calculate_pearson(data):
    num_cols = data.shape[1]
    matrix = np.zeros((num_cols, num_cols))
    for i in range(num_cols):
        for j in range(num_cols):
            mean = data.iloc[:, i].mean()
            std = data.iloc[:, i].std()
            mean2 = data.iloc[:, j].mean()
            std2 = data.iloc[:, j].std()
            matrix[i, j] = np.sum((data.iloc[:, i] - mean) * (data.iloc[:, j] - mean2)) / (
                    std * std2 * (data.shape[0] - 1))
    return pd.DataFrame(matrix, columns=data.columns, index=data.columns)


def get_percentages(eigenvalues):
    percentages = []
    for i in range(len(eigenvalues)):
        percentages.append((eigenvalues[i] / len(eigenvalues)) * 100)
    return percentages


def display_percentages_bar(percentages):
    plt.figure(figsize=(10, 6))
    plt.yticks(np.arange(0, 100, 5))
    plt.grid()
    plt.bar(range(len(percentages)), percentages, alpha=0.5, align='center', label='procent wartosci wlasnej')
    plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])
    plt.legend(loc='best')
    plt.xlabel('Numer składowej głównej')
    plt.ylabel('Procenty')
    plt.title('Procenty wartosci wlasnych')
    plt.show()
    plt.savefig('percentages_bar.png')


def display_percentages_line(percentages):
    plt.figure(figsize=(10, 6))
    plt.yticks(np.arange(0, 100, 5))
    plt.plot(range(len(percentages)), percentages, 'bo-', label='procent wartosci wlasnej')
    plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])
    values = np.arange(len(percentages))
    plt.xticks(values)
    plt.legend(loc='best')
    plt.grid()
    plt.xlabel('Numer składowej głównej')
    plt.ylabel('Procenty')
    plt.title('Procenty wartosci wlasnych')
    plt.show()
    plt.savefig('percentages_line.png')


def get_pca_matrix(eigenvectors, data):
    return np.dot(data, eigenvectors.T)


print('Reading data...')
data = pd.read_excel('data/dane_bio.xlsx')
row_names = data.iloc[:, 0]
print('Data read.')
print('Standardizing data...')
filtered_data = data.select_dtypes(include='number').columns
standardized_data = normalize_data(data)
standardized_data = pd.DataFrame(standardized_data, columns=filtered_data)
standardized_data.index = row_names

pearson = calculate_pearson(standardized_data)
eigenvalues, eigenvectors = np.linalg.eig(pearson)
eigenvalues = sorted(eigenvalues, reverse=True)
percentages = get_percentages(eigenvalues)
display_percentages_bar(percentages)
display_percentages_line(percentages)

figure = plt.figure(figsize=(10, 6))
sing_vals = np.arange(len(eigenvalues)) + 1
plt.plot(sing_vals, eigenvalues, 'ro-', linewidth=2)
plt.title('PCA')
plt.xlabel('Numer składowej głównej')
plt.ylabel('Wartosci wlasne')
plt.xticks(sing_vals)
plt.axhline(y=1, color='b', linestyle='--')
plt.grid()
plt.show()
plt.savefig('scree_plot.png')

pca_matrix = pd.DataFrame(get_pca_matrix(eigenvectors, standardized_data))
pca_matrix.columns = ['PC' + str(i + 1) for i in range(len(pca_matrix.columns))]
pca_matrix.index = row_names


def plot_pca(pca_matrix, first_var, second_var):
    plt.figure(figsize=(10, 6))
    plt.scatter(pca_matrix.iloc[:, first_var], pca_matrix.iloc[:, second_var], alpha=0.5)
    for i in range(len(pca_matrix)):
        plt.annotate(pca_matrix.index[i], (pca_matrix.iloc[i, first_var], pca_matrix.iloc[i, second_var]))
    plt.title('PCA')
    plt.xlabel('PC' + str(first_var + 1))
    plt.ylabel('PC' + str(second_var + 1))
    plt.grid()
    plt.show()
    plt.savefig(f'pcaPC{first_var + 1}-PC{second_var + 1}.png')


def plot_pca1_pc2(pca_matrix):
    plot_pca(pca_matrix, first_var=0, second_var=1)


def plot_pca1_pc3(pca_matrix):
    plot_pca(pca_matrix, first_var=0, second_var=2)


def plot_pca2_pc3(pca_matrix):
    plot_pca(pca_matrix, first_var=1, second_var=2)


plot_pca1_pc2(pca_matrix)
plot_pca1_pc3(pca_matrix)
plot_pca2_pc3(pca_matrix)


def get_charge_matrix(vectors, eigenvalues):
    charges = vectors * np.sqrt(eigenvalues)
    return pd.DataFrame(charges)


charge_matrix = get_charge_matrix(eigenvectors, eigenvalues)


def get_charge_matrix_bar_plot(charge_matrix, var):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(charge_matrix)), charge_matrix.iloc[:, var], alpha=0.5, align='center',
            label=f'{var + 1} składowa główna')
    plt.xticks(range(len(charge_matrix)), charge_matrix.index)
    plt.legend(loc='best')
    plt.xlabel('Zmienna')
    plt.ylabel('Wartosc ladunku czynnikowego')
    plt.title('Ladunki czynnikowe')
    plt.show()
    plt.savefig(f'charge_matrix_bar_PC{var + 1}.png')


get_charge_matrix_bar_plot(charge_matrix, var=0)
get_charge_matrix_bar_plot(charge_matrix, var=1)
get_charge_matrix_bar_plot(charge_matrix, var=2)


def get_cumulative_percentages(percentages):
    cumulative = []
    for i in range(len(percentages)):
        cumulative.append(sum(percentages[:i + 1]))
    return cumulative


def get_cumulative_plot(cumulative):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(cumulative)), cumulative, 'bo-', label='procent wartosci wlasnej')
    plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])
    values = np.arange(len(cumulative))
    plt.axhline(y=90, color='r', linestyle='--')
    plt.xticks(values)
    plt.legend(loc='best')
    plt.grid()
    plt.xlabel('Numer składowej głównej')
    plt.ylabel('Procent')
    plt.title('łączny procent wartosci wlasnych')
    plt.show()
    plt.savefig('cumulative_plot.png')


cumulative = get_cumulative_percentages(percentages)
get_cumulative_plot(cumulative)
