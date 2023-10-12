# Coding without library for clustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Data for clustering
x, y = datasets.load_iris(return_X_y=True)
x = x[:, :2]

# Build SVMs
class SVM:
    def __init__(self, lr=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = lr
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, x, y):
        n_samples, n_features = x.shape

        # Initialize parameters
        self.w = np.zeros(n_features)
        self.b = 0

        # Gradient descent
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(x):
                condition = y[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y[idx]))
                    self.b -= self.lr * y[idx]
                    
    def predict(self, x):
        linear_output = np.dot(x, self.w) - self.b
        return np.sign(linear_output)
    
    def plot_decision_boundary(self, x, y):
        # Plot data
        plt.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm')
        
        # Plot decision boundary
        x1 = np.linspace(np.min(x[:, 0]), np.max(x[:, 0]), 100)
        x2 = -(self.w[0] * x1 - self.b) / self.w[1]
        plt.plot(x1, x2, c='k')
        plt.show()
        
# Train
model = SVM()
model.fit(x, y)
model.plot_decision_boundary(x, y)