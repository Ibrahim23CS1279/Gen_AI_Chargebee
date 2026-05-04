# MATPLOTLIB VISUALIZATION EXAMPLES

import matplotlib.pyplot as plt
import numpy as np


# ==============================
# Line Plot
# ==============================

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(5, 4))
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ==============================
# Horizontal Bar Chart
# ==============================

categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.figure(figsize=(5, 4))
plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()


# ==============================
# Histogram
# ==============================

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.figure(figsize=(5, 4))
plt.hist(data, bins=4)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# ==============================
# Scatter Plot
# ==============================

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(5, 4))
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ==============================
# Pie Chart
# ==============================

sizes = [15, 30, 45, 10]

plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()


# ==============================
# Box Plot
# ==============================

data = [
    np.random.normal(size=100),
    np.random.normal(size=100)
]

plt.figure(figsize=(5, 4))
plt.boxplot(data)
plt.title("Box Plot")
plt.show()