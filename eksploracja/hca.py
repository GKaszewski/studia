import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt


def normalize_data(data):
    ids = data.iloc[:, 0]
    normalized = (data.iloc[:, 1:] - data.iloc[:, 1:].mean()) / data.iloc[:, 1:].std()
    return pd.concat([ids, normalized], axis=1)


print('Reading data...')
data = pd.read_excel('data/dane_bio.xlsx')
print('Data read.')
print('Standardizing data...')
filtered_data = data.select_dtypes(include='number').columns
standardized_data = normalize_data(data)
standardized_data = pd.DataFrame(standardized_data, columns=filtered_data)

numbers = standardized_data.values
matrix = np.zeros((30, 30))
for i in range(30):
    for j in range(30):
        matrix[i, j] = np.sqrt(np.sum((numbers[i] - numbers[j]) ** 2))
distances = pd.DataFrame(matrix)

coords = []
coords_names = []
min_vals_list = []
dictionary = {}
distances_copy = distances.copy()
names = []
name_cols = []
new_names = iter(range(30, 200, 1))
while distances.size >= 4:
    t = np.tril(distances, 0)
    diag = pd.DataFrame(t)
    flatten = np.array(diag).flatten()
    min_val = np.min(flatten[np.nonzero(flatten)])
    coordinates = np.where(diag == min_val)
    coord1 = max(coordinates)[0]
    coord2 = min(coordinates)[0]
    coords_list = distances.iloc[coord1].name, distances.iloc[coord2].name
    coords_names.append(coords_list)
    new_name = next(new_names)
    min_vals_list.append(min_val)

    for i in range(0, len(distances_copy)):
        name_cols.append(distances_copy.columns[i])
    if distances.iloc[coord1].name in name_cols and distances.iloc[coord2].name in name_cols:
        dictionary[new_name] = 2
    elif distances.iloc[coord1].name in name_cols and distances.iloc[coord2].name not in name_cols:
        dictionary[new_name] = 1 + dictionary.get(distances.iloc[coord2].name)
    elif distances.iloc[coord1].name not in name_cols and distances.iloc[coord2].name in name_cols:
        dictionary[new_name] = 1 + dictionary.get(distances.iloc[coord1].name)
    else:
        dictionary[new_name] = dictionary.get(distances.iloc[coord1].name) + dictionary.get(distances.iloc[coord2].name)

    vector = []
    for i in range(len(distances)):
        if distances.iloc[coord1, i] == 0:
            vector.append(distances.iloc[coord1, i])
        elif distances.iloc[coord2, i] == 0:
            vector.append(distances.iloc[coord2, i])
        elif distances.iloc[coord2, i] > distances.iloc[coord1, i]:
            vector.append(distances.iloc[coord2, i])
        else:
            vector.append(distances.iloc[coord1, i])

    distances.iloc[coord2] = vector
    distances.iloc[:, coord2] = vector

    distances.drop(distances.columns[coord1], axis=1, inplace=True)
    distances.drop(distances.index[coord1], axis=0, inplace=True)

    distances.rename(columns={distances.columns[coord2]: new_name}, inplace=True)
    distances.rename(index={distances.index[coord2]: new_name}, inplace=True)

dendrogram_data = []
p = list(dictionary.values())
for i in range(len(min_vals_list)):
    dendrogram_data.append([coords_names[i][0], coords_names[i][1], min_vals_list[i], p[i]])

scipy.cluster.hierarchy.dendrogram(dendrogram_data)
plt.savefig("dendrogram.png")
