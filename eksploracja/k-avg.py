import time

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def normalize_data(data):
    ids = data.iloc[:, 0]
    normalized = (data.iloc[:, 1:] - data.iloc[:, 1:].mean()) / data.iloc[:, 1:].std()
    return pd.concat([ids, normalized], axis=1)


print('Reading data...')
data = pd.read_excel('data/dane_bio.xlsx')
row_names = data.iloc[:, 0]
print('Data read.')
print('Standardizing data...')
filtered_data = data.select_dtypes(include='number').columns
standardized_data = normalize_data(data)
standardized_data = pd.DataFrame(standardized_data, columns=filtered_data)
standardized_data.index = row_names


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def plot_clusters(x, clusters, centroids, filename='k-avg.png'):
    plt.figure(figsize=(10, 6))
    plt.scatter(x[:, 0], x[:, 1], c=clusters, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')
    plt.title(f'K-means Clustering (k={len(centroids)})')   l
    plt.show()
    plt.savefig(filename)


class KMeans:
    def __init__(self, k, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations

    def initialize_centroids_randomly(self, x):
        np.random.shuffle(x)
        return x[:self.k]

    def initialize_centroids(self, x):
        return x[:self.k]

    def assign_clusters(self, x, centroids):
        clusters = []
        for _x in x:
            distances = [euclidean_distance(_x, centroid) for centroid in centroids]
            cluster = np.argmin(distances)
            clusters.append(cluster)
        return clusters

    def update_centroids(self, x, clusters):
        centroids = np.zeros((self.k, x.shape[1]))
        for cluster in range(self.k):
            cluster_points = [x[i] for i in range(len(x)) if clusters[i] == cluster]
            centroids[cluster] = np.mean(cluster_points, axis=0)
        return centroids

    def fit(self, x):
        centroids = self.initialize_centroids_randomly(x)
        for _ in range(self.max_iterations):
            clusters = self.assign_clusters(x, centroids)
            new_centroids = self.update_centroids(x, clusters)

            if np.all(centroids == new_centroids):
                break

            centroids = new_centroids
            plot_clusters(x, clusters, centroids, filename=f'kmeans/k-avg-{_}.png')

        self.centroids = centroids
        self.clusters = clusters


x = standardized_data.values
kmeans = KMeans(k=3)
kmeans.fit(x)

plot_clusters(x, kmeans.clusters, kmeans.centroids, filename='k-avg-best.png')
print(pd.DataFrame(kmeans.clusters, index=standardized_data.index))
pd.DataFrame(kmeans.centroids).to_json(f'k-avg-{int(time.time())}.json')
