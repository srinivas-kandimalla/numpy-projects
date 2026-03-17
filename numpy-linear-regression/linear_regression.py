import numpy as np

print("NumPy Linear Regression\n")

# Example dataset (X = house size, y = price)
X = np.array([1000, 1200, 1500, 1800, 2000])
y = np.array([50, 60, 75, 90, 100])

# Number of data points
n = len(X)

# Calculate mean
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate slope (m)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

m = numerator / denominator

# Calculate intercept (b)
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict value
def predict(x):
    return m * x + b

# Example prediction
x_new = 1600
y_pred = predict(x_new)

print("\nPredicted price for", x_new, "sqft:", y_pred)