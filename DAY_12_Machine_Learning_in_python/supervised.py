# SUPERVISED LEARNING IN PYTHON

# ==============================
# Linear Regression
# ==============================

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 2, 5, 4])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Output the coefficients and intercept
print("===== Linear Regression =====")
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# Plot the results
plt.figure(figsize=(6, 4))
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Simple Linear Regression")
plt.show()


# ==============================
# Logistic Regression
# ==============================

from sklearn.linear_model import LogisticRegression

# Example data
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([0, 0, 0, 0, 0,
              1, 1, 1, 1, 1])

# Create and train the model
model = LogisticRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Output the model parameters
print("\n===== Logistic Regression =====")
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", y_pred)

# Plot the results
plt.figure(figsize=(6, 4))
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict_proba(X)[:, 1], color='red')
plt.xlabel("X")
plt.ylabel("Probability of Class 1")
plt.title("Simple Logistic Regression")
plt.show()


# ==============================
# Decision Tree using Iris Dataset
# ==============================

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Initialize classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n===== Decision Tree =====")
print(f"Accuracy: {accuracy:.2f}")

# Visualize Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree - Iris Dataset")
plt.show()