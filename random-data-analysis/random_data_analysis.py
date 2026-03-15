import numpy as np

print("Random Data Analysis using NumPy\n")

# Generate random data
data = np.random.randint(10, 100, 10)

print("Random Data:")
print(data)

# Sum of values
total = np.sum(data)
print("\nTotal:", total)

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Maximum value
max_value = np.max(data)
print("Maximum:", max_value)

# Minimum value
min_value = np.min(data)
print("Minimum:", min_value)

# Standard deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
variance = np.var(data)
print("Variance:", variance)