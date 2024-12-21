# Linear Regression
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
    def mean_squared_error(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
    
    def r2_score(self, y_true, y_pred):
        return 1 - self.mean_squared_error(y_true, y_pred) / np.var(y_true)
    
    def plot(self, X, y):
        y_pred = self.predict(X)
        plt.scatter(X, y)
        plt.plot(X, y_pred, color='red')
        plt.show()
        
# Example
if __name__ == "__main__":
    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    import matplotlib.pyplot as plt

    # Data
    X, y = datasets.make_regression(n_samples = 100, n_features = 1, noise = 20, random_state = 4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 4856)

    # Model
    regressor = LinearRegression(lr = 0.001, n_iters = 1000)
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    # Evaluation
    print("MSE:", regressor.mean_squared_error(y_test, predictions))
    print("R2:", regressor.r2_score(y_test, predictions))

    # Plot
    regressor.plot(X, y)