# Coding without library for classification
import numpy as np
import matplotlib.pyplot as plt

# Data for decision tree
x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])  # Example labels for your data

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

    def fit(self, x, y):
        self.n_feats = x.shape[1] if not self.n_feats else min(self.n_feats, x.shape[1])
        self.root = self._grow_tree(x, y)

    def predict(self, x):
        return np.array([self._traverse_tree(x, self.root) for x in x])

    def _grow_tree(self, x, y, depth=0): # Recursion
        n_samples, n_features = x.shape
        n_labels = len(np.unique(y))

        # Stopping criteria
        if (depth >= self.max_depth
                or n_labels == 1
                or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)

        # Greedy search
        best_feat, best_thresh = self._best_criteria(x, y, feat_idxs)
        left_idxs, right_idxs = self._split(x[:, best_feat], best_thresh)

        left = self._grow_tree(x[left_idxs, :], y[left_idxs], depth + 1)
        right = self._grow_tree(x[right_idxs, :], y[right_idxs], depth + 1)
        return Node(best_feat, best_thresh, left, right)

    def _best_criteria(self, x, y, feat_idxs): # Greedy search
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            x_column = x[:, feat_idx]
            thresholds = np.unique(x_column)
            for threshold in thresholds:
                gain = self._information_gain(y, x_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
        return split_idx, split_thresh

    def _information_gain(self, y, x_column, split_thresh):
        # parent loss
        parent_entropy = self._entropy(y)

        # generate split
        left_idxs, right_idxs = self._split(x_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        
        # compute the weighted avg. of the loss for the children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r
        
        # information gain is difference in loss before vs. after split
        ig = parent_entropy - child_entropy
        return ig
    
    def _split(self, x_column, split_thresh):
        left_idxs = np.argwhere(x_column <= split_thresh).flatten()
        right_idxs = np.argwhere(x_column > split_thresh).flatten()
        return left_idxs, right_idxs
    
    def _entropy(self, y): # H = -sum(p * log(p))
        hist = np.bincount(y)
        ps = hist / np.sum(hist)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])
    
    def _most_common_label(self, y):
        hist = np.bincount(y)
        return np.argmax(hist)
    
    def _traverse_tree(self, x, node): # Recursion
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
    
    def plot(self, x, y):
        # Plot data
        plt.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm')

        # Plot decision boundary
        x1 = np.linspace(np.min(x[:, 0]), np.max(x[:, 0]), 100)
        x2 = np.linspace(np.min(x[:, 1]), np.max(x[:, 1]), 100)
        xx1, xx2 = np.meshgrid(x1, x2)
        x_grid = np.c_[xx1.ravel(), xx2.ravel()]
        y_pred = self.predict(x_grid).reshape(xx1.shape)
        plt.contourf(xx1, xx2, y_pred, alpha=0.5, cmap='coolwarm')
        plt.show()
        
# Train
tree = DecisionTree()
tree.fit(x, y)
tree.plot(x, y)