import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Data
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])  # Example labels for your data

plt.scatter(x[:, 0], x[:, 1])

# Calculate manhattan distance (can be fixed to p = 2 for Euclidean distance)
def manhattan_distance(x1, x2, p=1):
    return np.sum(np.abs(x1 - x2) ** p) ** (1 / p)

# Build K nearest neighbors
class KNN:
    def __init__(self, K=3):
        self.K = K

    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    def predict(self, x):
        predicted_labels = [self._predict(x_test) for x_test in x]
        return np.array(predicted_labels)

    def _predict(self, x_test):
        # Calculate distances
        distances = [manhattan_distance(x_test, x_train) for x_train in self.x_train]

        # Get K nearest samples, labels
        k_indices = np.argsort(distances)[:self.K]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def plot_distance_point_to_k(self, x, y):
        # Plot data
        plt.scatter(self.x_train[:, 0], self.x_train[:, 1], c=self.y_train, cmap='coolwarm')

        # Plot distance to K
        for i in range(len(x)):
            distances = [manhattan_distance(x[i], x_train) for x_train in self.x_train]
            k_indices = np.argsort(distances)[:self.K]
            for j in k_indices:
                plt.plot([x[i][0], self.x_train[j][0]], [x[i][1], self.x_train[j][1]], c='k', alpha=0.3)
        plt.show()

# Train
knn = KNN(K = 3)
knn.fit(x, y)
y_pred = knn.predict(x)
knn.plot_distance_point_to_k(x, y)