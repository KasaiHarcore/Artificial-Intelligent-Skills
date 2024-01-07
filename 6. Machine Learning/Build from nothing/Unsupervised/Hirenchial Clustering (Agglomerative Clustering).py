# Coding without library
import numpy as np
import matplotlib.pyplot as plt

# Data for Hierarchical Clustering
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
plt.scatter(x[:, 0], x[:, 1])

# Calculate euclidean distance
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Build Hierarchical Clustering
class AgglomerativeClustering():
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters
        self.clusters = [[i] for i in range(len(x))]  # Initialize each point as a cluster
        self.labels = np.zeros(len(x))

    def predict(self, x):
        self.x = x
        self.n_samples, self.n_features = x.shape

        # Merge clusters
        while len(self.clusters) > self.n_clusters:
            # Calculate distance between clusters
            distances = []
            for i in range(len(self.clusters)):
                for j in range(i + 1, len(self.clusters)):
                    distances.append((euclidean_distance(self.clusters[i][0], self.clusters[j][0]), i, j))
            distances.sort(key=lambda x: x[0])

            # Merge clusters
            _, i, j = distances[0]
            self.clusters[i] += self.clusters[j]
            self.clusters.pop(j)

        # Return cluster labels and save them
        self.labels = self._get_cluster_labels(self.clusters)
        return self.labels

    def _get_cluster_labels(self, clusters):
        labels = np.zeros(self.n_samples)
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx
        return labels

    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        for i, index in enumerate(self.clusters):
            point = self.x[index].T
            ax.scatter(*point)
        plt.show()

# Train
cluster = AgglomerativeClustering(n_clusters=2)
cluster.predict(x)
cluster.plot()

# Access cluster labels
print("Cluster Labels:", cluster.labels)
