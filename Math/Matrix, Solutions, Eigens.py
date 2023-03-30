# To create a matrix using NumPy, you can use the numpy.array() function. Here's an example: 
# If you got error of numpy try to install/reinstall it with: " ipython pip3 install numpy " / or just " pip3 install numpy"
import numpy as np

# Create a 2x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# You can see that the format of the syntax is: np.(attribut) then followed by ( [  [],[], ..., []   ]  ). 
# So there is a big bracket that contains small brackets indicating raws of a matrix.

# To print the result
print(matrix)

#Here is the output:
[[1 2 3]
 [4 5 6]]

#You can also create matrices of zeros or ones using the numpy.zeros() and numpy.ones() functions. Here's an example: 
zeros_matrix = np.zeros((3, 3))
print(zeros_matrix)

# Output:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

# Create a 2x4 matrix of ones
ones_matrix = np.ones((2, 4))
print(ones_matrix)

# Output:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

# Basic math operations in python for matrix

# Matrix addition and subtraction: You can add or subtract two matrices of the same size by using the + and - operators, respectively. 
# Here's an example:

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix addition
c = a + b
print(c)

# Output
[[ 6  8]
 [10 12]]

# Matrix subtraction
d = a - b
print(d)

# Output
[[-4 -4]
 [-4 -4]]

# Matrix multiplication: You can multiply two matrices using the numpy.dot function.
# Note that matrix multiplication is not the same as element-wise multiplication. Here's an example:
c = np.dot(a, b)
print(c)

# Output
[[19 22]
 [43 50]]

# Element-wise multiplication: To perform element-wise multiplication, you can use the * operator or the numpy.multiply function.
# Here's an example:
c = a * b
d = np.multiply(a, b)

print(c)
print(d)

# Output
[[ 5 12]
 [21 32]]

[[ 5 12]
 [21 32]]

# Element-wise division: To perform element-wise division, you can use the / operator or the numpy.divide function. Here's an example:
c = a / b
d = np.divide(a, b)

print(c)
print(d)

# Output
[[0.2        0.33333333]
 [0.42857143 0.5       ]]

[[0.2        0.33333333]
 [0.42857143 0.5       ]]


# Transpose of a matrix: You can obtain the transpose of a matrix using the numpy.transpose function. Here's an example:
b = np.transpose(a)
print(b)
# Output
[[1 3]
 [2 4]]

# Inverse of a matrix: You can obtain the inverse of a matrix using the numpy.linalg.inv function. 
# Note that not all matrices have an inverse. Here's an example:

b = np.linalg.inv(a)
print(b)

# Output
[[-2.   1. ]
 [ 1.5 -0.5]]

# To calculate the determinant of a matrix using NumPy, you can use the numpy.linalg.det function. Here's an example:
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
det = np.linalg.det(a)

print(det)
# Output
0.0

'''
In this example, we created a 3x3 matrix a and calculated its determinant using the numpy.linalg.det function. 
The result is 0.0, which indicates that the matrix is singular (i.e., not invertible).
Note that the determinant of a singular matrix is always zero.
If you need to compute the determinant of a larger matrix, you can use the same function by providing the matrix as an input. 
The numpy.linalg.det function works for matrices of any size, but computing the determinant of large matrices can be computationally expensive and may require a significant amount of memory.

It's worth noting that NumPy provides many other linear algebra functions that can be useful for working with matrices, 
such as numpy.linalg.inv for computing the inverse of a matrix, numpy.linalg.eig for computing the eigenvalues and eigenvectors of a matrix, 
and many others.
'''

# To find the solutions of a matrix, you can use the Gaussian elimination method or other similar techniques from linear algebra. 
# However, in NumPy, you can solve a system of linear equations represented as a matrix equation by using the numpy.linalg.solve function. 
# Here's an example:

# Create a matrix of coefficients
a = np.array([[2, 3], [4, 5]])

# Create a column vector of constants
b = np.array([7, 10])

# Solve the system of linear equations
x = np.linalg.solve(a, b)

print(x)

# OutPut
[1. 2.]

'''
In this example, we created a matrix a of coefficients and a column vector b of constants. 
We then used the numpy.linalg.solve function to solve the system of linear equations represented by the matrix equation ax = b. 
The solution x is a row vector containing the values of the variables that satisfy the system of linear equations.

Note that the numpy.linalg.solve function expects the input matrix a to be square and non-singular (i.e., invertible). 
If the matrix is not invertible or the system of linear equations has no solution or infinite solutions, the function will raise a LinAlgError.

'''

# To find the eigenvectors and eigenvalues of a matrix using NumPy, you can use the numpy.linalg.eig function. Here's an example:

# Create a Matrix
a = np.array([[1, 2], [3, 4]])

# Find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(a)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

# Output
Eigenvalues:
[-0.37228132  5.37228132]
Eigenvectors:
[[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]

'''
In this example, we created a 2x2 matrix a and used the numpy.linalg.eig function to find its eigenvalues and eigenvectors. 
The eigenvalues variable contains a 1D array of the two eigenvalues, while the eigenvectors variable contains a 2D array of the two eigenvectors, each represented as a column of the array.

It's worth noting that NumPy uses a different convention for eigenvectors than some other linear algebra software. 
Specifically, the eigenvectors returned by NumPy are not normalized to unit length. 
If you need to normalize the eigenvectors, you can do so manually by dividing each vector by its length.

Also, note that the numpy.linalg.eig function works only for square matrices. 
If the input matrix is not square or is singular, the function will raise a LinAlgError.

'''
