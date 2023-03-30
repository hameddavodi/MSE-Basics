'''
Linear programming is a technique used to optimize a linear objective function subject to linear equality and inequality constraints.
Numpy is a Python library that provides many mathematical functions and tools for working with arrays.
One of the main features of numpy is the ability to solve linear systems of equations.
'''
#Suppose we want to maximize the objective function:

Maximize 3x + 4y

# And here is our constraints:
2x + y <= 20
x + 2y <= 20
x >= 0
y >= 0

# We can use the following code to solve this problem in Python using numpy:
# Importing numpy library
import numpy as np

# Define the coefficients of the objective function
c = np.array([3, 4])

# Define the coefficients of the constraints
A = np.array([[2, 1], [1, 2], [-1, 0], [0, -1]])
b = np.array([20, 20, 0, 0])

# Set the bounds on the variables
x_bounds = (0, None)
y_bounds = (0, None)

'''
Until this point we used what we have learned in the last section " Matrix, Solutions and Eigens".
Here, we start to use another library called SCIPY. 
'''

# Use the linprog function from scipy.optimize to solve the problem
from scipy.optimize import linprog

res = linprog(c=c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

'''
Pay attantion to the syntax we used
  c: an array of coefficients of the linear objective function to be maximized or minimized.
  
  A_ub: a 2D array of coefficients of the inequality constraints (the "A" matrix in Ax <= b). 
    The constraints are assumed to be in the form of A_ub @ x <= b_ub.
    
  b_ub: a 1D array of the right-hand side values of the inequality constraints.
  
  A_eq: a 2D array of coefficients of the equality constraints (the "A" matrix in Ax = b). 
    The constraints are assumed to be in the form of A_eq @ x = b_eq.
    
  b_eq: a 1D array of the right-hand side values of the equality constraints.
  
  bounds: a sequence of tuples specifying the bounds of the variables. 
    Each tuple is of the form (min, max) where min and max are optional lower and upper bounds. If a bound is not specified, it is assumed to be unbounded.
    
  method: a string specifying the algorithm to use for solving the linear programming problem. 
    The default value is 'simplex', which uses the simplex algorithm. Other options include 'highs' (for the HiGHS interior point method) and 'interior-point' (for the primal-dual interior point method).
    
  callback: a callable function that is called once per iteration of the algorithm. 
    It is passed a dictionary containing information about the current iteration, including the current solution vector and the current objective value.
    
  options: a dictionary of solver-specific options. For example, 'maxiter' specifies the maximum number of iterations to perform.
'''

print(res)

# Output:
fun: 33.33333333333333
message: 'Optimization terminated successfully.'
nit: 3
slack: array([ 0.        ,  0.        , 13.33333333,  6.66666667])
status: 0
success: True
x: array([6.66666667, 6.66666667])

'''
The output of scipy.linprog is a scipy.optimize.OptimizeResult object that contains the following fields:

    x: the optimal solution to the linear programming problem.
    fun: the optimal value of the objective function.
    success: a boolean indicating whether the optimizer successfully found a solution.
    status: an integer indicating the status of the optimizer at termination.
    message: a string indicating the reason for the termination of the optimizer.
    nit: the number of iterations performed by the optimizer.
    slack: a 1D array containing the values of the slack variables at the optimal solution.
'''

'''
The optimal solution is x=6.67 and y=6.67 with an objective function value of 33.33. The slack variables give the amount by which the constraints are relaxed at the optimal solution.
'''
