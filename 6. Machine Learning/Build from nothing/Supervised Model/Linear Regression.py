# Coding without library
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

class LinearRegression():
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias
        
    def forward(self, x):
        return self.weight * x + self.bias
    
    def loss(self, y_pred, y):
        return np.mean((y_pred - y)**2)
    
    def gradient(self, x, y_pred, y):
        return np.mean(2 * (y_pred - y) * x), np.mean(2 * (y_pred - y))
    
    def update(self, grad_w, grad_b, lr):
        self.weight -= lr * grad_w
        self.bias -= lr * grad_b
        
    def train(self, x, y, lr, epoch):
        for i in range(epoch):
            y_pred = self.forward(x)
            loss = self.loss(y_pred, y)
            grad_w, grad_b = self.gradient(x, y_pred, y)
            self.update(grad_w, grad_b, lr)
            if i % 50 == 0:
                print("Epoch: {}, Loss: {:.3f}".format(i+1, loss))
            
model = LinearRegression(0, 0)
model.train(x, y, 0.01, 500)

# Plot
plt.scatter(x, y)
plt.plot(x, model.forward(x), c='r')
plt.show()