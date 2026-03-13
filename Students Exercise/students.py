# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Import data
students = pd.read_csv('students.csv')


# Print first few rows of data
print(students.head(5))


# Print summary statistics for all columns
print(students.describe(include = 'all'))

# Calculate mean
student_mean = students.math_grade.mean()
print(student_mean)

# Calculate median
student_median = students.math_grade.median()
print(student_median)

# Calculate mode
student_mode = students.math_grade.mode()
print(student_mode)

# Calculate range
student_range = students.math_grade.max() - students.math_grade.min()
print(student_range)

# Calculate standard deviation
student_std = students.math_grade.std()
print(student_std)

# Calculate MAD
student_mad = students.math_grade.mad()
print(student_mad)

#Consider adding brief comments or print statements to interpret your findings, especially when comparing mean, median, and mode. Example:
print(f"Mean: {student_mean}, Median: {student_median}, Mode: {student_mode[0]}")
print("The mean and median are close, suggesting a fairly symmetric distribution.")

#Consider handling cases where there may be multiple modes in the math_grade column, as .mode() can return more than one value. Example:
if len(student_mode) > 1:
    print(f"Modes: {list(student_mode)}")
else:
    print(f"Mode: {student_mode[0]}")

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
mjob_count = students.Mjob.value_counts()

# Calculate proportion of students with mothers in each job category
mjob_proportion = students.Mjob.value_counts(normalize=True)

# Create bar chart of Mjob
bar_chart = sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
pie_chart = students.Mjob.value_counts().plot.pie()
plt.show()

# Example for 'address' column
print(students.address.value_counts())
sns.countplot(x='address', data=students)
plt.show()
plt.clf()

# Example for 'absences' column
print(students.absences.describe())
sns.histplot(x='absences', data=students)
plt.show()
plt.clf()

# Example for 'Fjob' column
print(students.Fjob.value_counts())
sns.countplot(x='Fjob', data=students)
plt.show()
plt.clf()