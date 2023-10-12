import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, num_features, learning_rate=0.1, num_epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.zeros(num_features)
        self.bias = 0
    
    def predict(self, x):
        # Compute the weighted sum and add bias
        activation = np.dot(self.weights, x) + self.bias
        # Apply the step function (1 if activation >= 0, 0 otherwise)
        return 1 if activation >= 0 else 0
    
    def train(self, X, y):
        for epoch in range(self.num_epochs):
            misclassified = 0
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                if error != 0:
                    misclassified += 1
                    # Update weights and bias
                    self.weights += self.learning_rate * error * X[i] # Perceptron update rule
                    self.bias += self.learning_rate * error
            if misclassified == 0:
                print(f"Converged after {epoch+1} epochs.")
                return
        print("Perceptron did not converge.")
    
    def plot_predict_line(self, X, y):
        # Plot data
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
        # Plot predict line
        x1 = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
        x2 = -(self.weights[0] * x1 + self.bias) / self.weights[1]
        plt.plot(x1, x2, c='k')
        plt.show()

# Example usage:
# Define training data (X) and corresponding labels (y)
X = np.array([[2, 3], [1, 4], [3, 1], [4, 2], [3, 3], [2, 1], [1, 2]]) # 2D
y = np.array([1, 1, 0, 0, 1, 0, 0]) # 1: red, 0: blue

# Create a Perceptron model and train it
model = Perceptron(num_features=2)
model.train(X, y)

# Test the trained model
test_data = np.array([[2, 2], [3, 3], [1, 1]])
for x in test_data:
    prediction = model.predict(x)
    print(f"Input: {x}, Prediction: {prediction}")
    
# Plot predict line
model.plot_predict_line(X, y)