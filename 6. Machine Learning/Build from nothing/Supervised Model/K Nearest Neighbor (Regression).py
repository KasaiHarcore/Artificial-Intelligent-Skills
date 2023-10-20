# For regression task
class KNNRegressor:
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

        # Average
        return np.mean(k_nearest_labels)
    
# Train
knn = KNNRegressor(K = 3)
knn.fit(x, y)
y_pred = knn.predict(x)

# Plot
plt.scatter(x[:, 0], x[:, 1])
plt.scatter(x[:, 0], y_pred, c='r')
plt.show()