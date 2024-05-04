import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    return np.sqrt(sum((point1 - point2) ** 2))


class Cluster:
    def __init__(self, idx, points, linkage):
        self.idx = idx
        self.points = points
        self.linkage = linkage
        self.centroid = np.mean(points, axis=0)
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Cluster {self.idx}'

    def merge(self, other):
        merged_points = np.vstack((self.points, other.points))
        return Cluster(self.idx, merged_points, self.linkage)


def complete_linkage(clusters):
    num_clusters = len(clusters)
    distances = np.zeros((num_clusters, num_clusters))

    for i in range(num_clusters):
        for j in range(i + 1, num_clusters):
            distances[i, j] = np.max(
                [euclidean_distance(p1, p2) for p1 in clusters[i].points for p2 in clusters[j].points])
            distances[j, i] = distances[i, j]

    return distances


def single_linkage(clusters):
    num_clusters = len(clusters)
    distances = np.zeros((num_clusters, num_clusters))

    for i in range(num_clusters):
        for j in range(i + 1, num_clusters):
            dist = np.min([euclidean_distance(p1, p2) for p1 in clusters[i].points for p2 in clusters[j].points])
            distances[i, j] = dist
            distances[j, i] = dist

    return distances


def hca(data, linkage_func):
    print('HCA started.')
    clusters = [Cluster(idx=i, points=np.array([data[i]]), linkage=linkage_func) for i in range(len(data))]

    while len(clusters) > 1:
        print(f'Number of clusters: {len(clusters)}')
        distances = linkage_func(clusters)
        np.fill_diagonal(distances, np.inf)
        i, j = np.unravel_index(distances.argmin(), distances.shape)
        merged_cluster = clusters[i].merge(clusters[j])
        print(f'Merged cluster {clusters[i]} and {clusters[j]} into {merged_cluster}.')
        merged_cluster.left = clusters[i]
        merged_cluster.right = clusters[j]

        clusters = [merged_cluster if idx in (i, j) else c for idx, c in enumerate(clusters) if idx != j]
    print('HCA finished.')
    return clusters[0]


def print_leaves(cluster):
    if cluster.left is None and cluster.right is None:
        print('leaf ' + str(cluster.idx))
        print(cluster.points)

    if cluster.left is not None:
        print('left ' + str(cluster.left.idx))
        print_leaves(cluster.left)

    if cluster.right is not None:
        print('right ' + str(cluster.right.idx))
        print_leaves(cluster.right)


def generate_dendrogram(dendrogram):
    fig, ax = plt.subplots(figsize=(10, 5))

    # determine the x-position of each node in the dendrogram
    node_positions = {}
    node_count = 0
    for i, merge_info in dendrogram.items():
        left_pos = node_positions.get(merge_info['left'], 0)
        right_pos = node_positions.get(merge_info['right'], 0)
        node_positions[i] = (left_pos + right_pos) / 2
        node_count += 1

    # plot the dendrogram
    for i, merge_info in dendrogram.items():
        left_pos = node_positions[merge_info['left']]
        right_pos = node_positions[merge_info['right']]
        distance = merge_info['distance']
        ax.plot([left_pos, left_pos, right_pos, right_pos], [0, distance, distance, 0], '-')

    ax.set_xlim(0, node_positions[node_count - 1])
    ax.set_ylim(0, max(merge_info['distance'] for merge_info in dendrogram.values()))

    ax.set_xlabel('Index')
    ax.set_ylabel('Distance')

    plt.show()


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
print(standardized_data)
print('Data standardized.')
print('Clustering...')
clusters = [Cluster(idx=i, points=np.array([standardized_data.iloc[i].values]), linkage=complete_linkage) for i in
            range(len(standardized_data))]
root = hca(standardized_data.values, complete_linkage)
print('Clustering finished.')
print('Printing leaves...')
print_leaves(root)
print('root', root)
print('Leaves printed.')
print(f'root shape: {root.points.shape}')