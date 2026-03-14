import numpy as np

print("Matrix Calculator using NumPy\n")

# Input matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
addition = A + B
print("\nMatrix Addition (A + B):")
print(addition)

# Subtraction
subtraction = A - B
print("\nMatrix Subtraction (A - B):")
print(subtraction)

# Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (A × B):")
print(multiplication)

# Transpose
transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)

# Determinant
det_A = np.linalg.det(A)
print("\nDeterminant of Matrix A:")
print(det_A)