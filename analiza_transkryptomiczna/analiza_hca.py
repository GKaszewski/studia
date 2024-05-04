import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist

data = pd.read_excel('data/Dane_Eggplants_Percent.xlsx')

features = data.columns[1:]
x = data.loc[:, features].values
x = StandardScaler().fit_transform(x)

distance_matrix = pdist(x, metric='euclidean')

linkage_matrix = linkage(distance_matrix, method='average')

plt.figure(figsize=(10, 14))
dendrogram(linkage_matrix, labels=data.iloc[:, 0].values, leaf_rotation=90)
plt.title('Dendrogram (Average)')
plt.show()
