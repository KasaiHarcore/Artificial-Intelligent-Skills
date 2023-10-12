# Coding without library for regression
import numpy as np
import matplotlib.pyplot as plt

# Data for decision tree
x = np.linspace(-5, 5, 100)
y = np.sin(x) + np.random.rand(100) - 0.5

# Build decision tree
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_feats=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats
        self.root = None

    def fit(self, X, y):
        # Store the number of features if not specified
        if self.n_feats is None:
            self.n_feats = X.shape[1]

        # Build the tree
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        # Stopping criteria
        if depth >= self.max_depth or n_samples < self.min_samples_split:
            leaf_value = np.mean(y)
            return Node(value=leaf_value)

        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)

        # Choose the best feature and threshold
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)

        # Recursively build the left and right subtrees
        left_subtree = self._build_tree(X[left_idxs], y[left_idxs], depth + 1)
        right_subtree = self._build_tree(X[right_idxs], y[right_idxs], depth + 1)

        # Return the current node
        return Node(best_feat, best_thresh, left_subtree, right_subtree)

    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
        return split_idx, split_thresh

    def _information_gain(self, y, X_column, split_thresh):
        parent_entropy = self._entropy(y)
        left_idxs, right_idxs = self._split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        left_entropy = self._entropy(y[left_idxs])
        right_entropy = self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * left_entropy + (n_r / n) * right_entropy

        ig = parent_entropy - child_entropy
        return ig

    def _entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / counts.sum()
        entropy = sum([-p * np.log2(p) for p in probabilities])
        return entropy

    def _split(self, X_column, split_thresh):
        left_idxs = np.where(X_column <= split_thresh)[0]
        right_idxs = np.where(X_column > split_thresh)[0]
        return left_idxs, right_idxs

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

# Create and train the DecisionTree model
model = DecisionTree(max_depth=5)
model.fit(x.reshape(-1, 1), y)

# Make predictions
x_test = np.linspace(-5, 5, 1000)
y_pred = model.predict(x_test.reshape(-1, 1))

# Plot the original data and the predicted values
plt.scatter(x, y, label='Data')
plt.plot(x_test, y_pred, label='Predictions', color='red')
plt.legend()
plt.show()