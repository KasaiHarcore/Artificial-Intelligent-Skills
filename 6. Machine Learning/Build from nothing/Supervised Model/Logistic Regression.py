# Coding without library
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])  # Example labels for your data

# Build
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class LogisticRegression():
    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def fit(self, x, y):
        # Init parameters
        n_samples, n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for _ in range(self.n_iters):
            # forward processing
            linear_model = np.dot(x, self.weights) + self.bias
            y_pred = sigmoid(linear_model)
            
            # Derivatives
            dw = (1 / n_samples) * np.dot(x.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_model)
        y_pred_cls = [1 if i > 0.5 else 0 for i in y_pred]
        return np.array(y_pred_cls)
    
    def plot(self, X, y):
        # Plot data
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
        # Plot predict line
        x1 = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
        x2 = -(self.weights[0] * x1 + self.bias) / self.weights[1]
        plt.plot(x1, x2, c='k')
        plt.show()

# Train
model = LogisticRegression(lr = 0.01, n_iters = 1000)
model.fit(x, y)

# Plot
model.plot(x, y)