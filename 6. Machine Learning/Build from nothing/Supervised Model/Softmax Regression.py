import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])  # Example labels for your data

# Build
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

class SoftmaxRegression():
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def fit(self, x, y):
        # Init parameters
        n_samples, n_features = x.shape
        n_classes = len(np.unique(y))
        self.weights = np.zeros((n_features, n_classes))
        self.bias = np.zeros(n_classes)

        # Gradient descent
        for _ in range(self.n_iters):
            # Forward processing
            linear_model = np.dot(x, self.weights) + self.bias
            y_pred = softmax(linear_model)

            # Derivatives
            dw = (1 / n_samples) * np.dot(x.T, (y_pred - y.reshape(-1, 1)))
            db = (1 / n_samples) * np.sum(y_pred - y.reshape(-1, 1), axis=0)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = softmax(linear_model)
        return np.argmax(y_pred, axis=1)
    
    def plot_decision_boundary(self, X, y):
        # Plot data
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
        
        # Create a meshgrid to plot decision boundary
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.1), np.arange(x2_min, x2_max, 0.1))
        Z = self.predict(np.c_[xx1.ravel(), xx2.ravel()])
        Z = Z.reshape(xx1.shape)
        
        # Plot decision boundary
        plt.contourf(xx1, xx2, Z, alpha=0.4, cmap='coolwarm')
        plt.show()

# Train
model = SoftmaxRegression(lr=0.01, n_iters=1000)
model.fit(x, y)

# Plot decision boundary
model.plot_decision_boundary(x, y)