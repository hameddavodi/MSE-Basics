'''
Matrix, solutions, and eigens are all essential concepts in linear algebra, which is a crucial field in data science.
Matrices are rectangular arrays of numbers that can be used to represent data sets, with each element in the matrix representing a single data point.
Solutions in linear algebra refer to finding the values of the variables in a system of linear equations that satisfy all the equations simultaneously.
This is important in data science, where linear models are often used to represent and analyze data.
Eigens are a way of describing the characteristics of a matrix, and they are often used in dimensionality reduction techniques such as principal component analysis.
By finding the eigens of a matrix, we can identify the most important features of the data and reduce its complexity, making it easier to work with and analyze
'''


'''
To create a matrix using NumPy, you can use the numpy.array() function. Here's an example:
''' 

import numpy as np

# Create a 2x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# You can see that the format of the syntax is: np.(attribut) then followed by ( [  [],[], ..., []   ]  ). 
# So there is a big bracket that contains small brackets indicating raws of a matrix.

print(matrix)
#Here is the output:
###################################################

[[1 2 3]
 [4 5 6]]

###################################################

#You can also create matrices of zeros or ones using the numpy.zeros() and numpy.ones() functions:

import numpy as np

# Create a 3x3 matrix of zeros
zeros_matrix = np.zeros((3, 3))

print(zeros_matrix)

###################################################
# Output:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

# Create a 2x4 matrix of ones
ones_matrix = np.ones((2, 4))

print(ones_matrix)
###################################################
# Output:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

