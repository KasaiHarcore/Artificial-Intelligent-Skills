# K-Means
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
X = data.data

class K_Means():
    def __init__(self, k = 3, max_iter = 100):
        self.k = k
        self.max_iter = max_iter

    def fit(self, X):
        self.X = X
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace = False)]
        self.clusters = np.zeros(X.shape[0])
        for _ in range(self.max_iter):
            for x in range(X.shape[0]):
                distances = np.linalg.norm(X[x] - self.centroids, axis = 1)
                self.clusters[x] = np.argmin(distances)
            for i in range(self.k):
                self.centroids[i] = np.mean(X[self.clusters == i], axis = 0)
        plt.scatter(X[:, 0], X[:, 1], c = self.clusters, cmap = 'viridis')
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c = 'red')
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()
                
model = K_Means(k = 5)
model.fit(X)