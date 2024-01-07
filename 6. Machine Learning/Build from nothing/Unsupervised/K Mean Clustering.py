# Coding without library
import numpy as np
import matplotlib.pyplot as plt

# Data for Kmeans
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
plt.scatter(x[:, 0], x[:, 1])

# Calculate euclidean distance
def euclidean_distance(x1 , x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Build Kmeans
class KMeans():
    def __init__(self, K = 2, max_iter = 100, plot_steps = False):
        self.K = K
        self.max_iter = max_iter
        self.plot_step = plot_steps
        self.clusters = [[] for _ in range(self.K)]
        self.centroids = []
        
    def predict(self, x):
        self.x = x
        self.n_samples, self.n_features = x.shape
        
        # Initialize centroids
        random_sample_idxs = np.random.choice(self.n_samples, self.K, replace = False)
        self.centroids = [self.x[idx] for idx in random_sample_idxs]
        
        # Optimize clusters
        for _ in range(self.max_iter):
            # Update clusters
            self.clusters = self._create_clusters(self.centroids)
            
            if self.plot_step:
                self.plot()
                
            # Update centroids
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            
            # Check if converged
            if self._is_converged(centroids_old, self.centroids):
                break
                
            if self.plot_step:
                self.plot()
                
        # Return cluster labels
        return self._get_cluster_labels(self.clusters)
    
    def _get_cluster_labels(self, clusters):
        labels = np.empty(self.n_samples)
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx
        return labels
    
    def _create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.x):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)
        return clusters
    
    def _closest_centroid(self, sample, centroids):
        distances = [euclidean_distance(sample, point) for point in centroids]
        closest_idx = np.argmin(distances)
        return closest_idx
    
    def _get_centroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.x[cluster], axis = 0)
            centroids[cluster_idx] = cluster_mean
        return centroids
    
    def _is_converged(self, centroids_old, centroids):
        distances = [euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)]
        return sum(distances) == 0
    
    def plot(self):
        fig, ax = plt.subplots(figsize = (12, 8))
        for i, index in enumerate(self.clusters):
            point = self.x[index].T
            ax.scatter(*point)
        for point in self.centroids:
            ax.scatter(*point, marker = "x", color = "black", linewidth = 2)
        plt.show()
        
# Train
kmeans = KMeans(K = 2, max_iter = 150, plot_steps = True)
y_pred = kmeans.predict(x)