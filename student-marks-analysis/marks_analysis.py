import numpy as np

# Student marks for 5 students in 3 subjects
marks = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [65, 70, 72],
    [90, 92, 95],
    [55, 60, 58]
])

print("Student Marks:")
print(marks)

# Average marks per student
avg_student = np.mean(marks, axis=1)
print("\nAverage marks per student:")
print(avg_student)

# Average marks per subject
avg_subject = np.mean(marks, axis=0)
print("\nAverage marks per subject:")
print(avg_subject)

# Highest mark in dataset
print("\nHighest mark:", np.max(marks))

# Lowest mark
print("Lowest mark:", np.min(marks))

# Top student
top_student = np.argmax(avg_student)

print("\nTop student index:", top_student)