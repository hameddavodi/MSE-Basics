## Linear Programming
Suppose we want to maximize the objective function:

Maximize `3x + 4y`

And here is our constraints:

`2x + y <= 20`
`x + 2y <= 20`
`x >= 0`
`y >= 0`

We can use the following code to solve this problem in Python using numpy:
```python
import numpy as np

# Define the coefficients of the objective function
c = np.array([3, 4])

# Define the coefficients of the constraints
A = np.array([[2, 1], [1, 2], [-1, 0], [0, -1]])
b = np.array([20, 20, 0, 0])

# Set the bounds on the variables
x_bounds = (0, None)
y_bounds = (0, None)
```

Use the linprog function from `scipy.optimize` to solve the problem
```python

from scipy.optimize import linprog

res = linprog(c=c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])
print(res)
```

Pay attantion to the syntax we used
  `c`: an array of coefficients of the linear objective function to be maximized or minimized.
  
  `A_ub`: a 2D array of coefficients of the inequality constraints (the "`A`" matrix in `Ax <= b`). 
    The constraints are assumed to be in the form of `A_ub @ x <= b_ub`.
    
  `b_ub`: a 1D array of the right-hand side values of the inequality constraints.
  
  `A_eq`: a 2D array of coefficients of the equality constraints (the "`A`" matrix in `Ax = b`). 
    The constraints are assumed to be in the form of `A_eq @ x = b_eq`.
    
  `b_eq`: a 1D array of the right-hand side values of the equality constraints.
  
  `bounds`: a sequence of tuples specifying the bounds of the variables. 
    Each tuple is of the form (`min, max`) where min and max are optional lower and upper bounds. If a bound is not specified, it is assumed to be unbounded.
    
  `method`: a string specifying the algorithm to use for solving the linear programming problem. 
    The default value is '`simplex`', which uses the simplex algorithm. Other options include '`highs`' (for the HiGHS interior point method) and '`interior-point`' (for the primal-dual interior point method).
    
  `callback`: a callable function that is called once per iteration of the algorithm. 
    It is passed a dictionary containing information about the current iteration, including the current solution vector and the current objective value.
    
  `options`: a dictionary of solver-specific options. For example, '`maxiter`' specifies the maximum number of iterations to perform.

```python
# Output:
fun: 33.33333333333333
message: 'Optimization terminated successfully.'
nit: 3
slack: array([ 0.        ,  0.        , 13.33333333,  6.66666667])
status: 0
success: True
x: array([6.66666667, 6.66666667])
```

The output of `scipy.linprog` is a `scipy.optimize.OptimizeResult` object that contains the following fields:
```python
'''
    x: the optimal solution to the linear programming problem.
    fun: the optimal value of the objective function.
    success: a boolean indicating whether the optimizer successfully found a solution.
    status: an integer indicating the status of the optimizer at termination.
    message: a string indicating the reason for the termination of the optimizer.
    nit: the number of iterations performed by the optimizer.
    slack: a 1D array containing the values of the slack variables at the optimal solution.
```
The optimal solution is `x=6.67` and `y=6.67` with an objective function value of `33.33`. The slack variables give the amount by which the constraints are relaxed at the optimal solution.

## Dynamic Systems
Dynamic systems are systems that evolve over time, and they can be described by a set of differential equations. In Python, we can solve these equations and graph the results using the NumPy and Matplotlib libraries.

Suppose we want to solve the following system of differential equations:

`dx/dt = -2x + y`
`dy/dt = -x - 2y`

With initial conditions `x(0) = 1` and `y(0) = 0`.

We can use the following code to solve this system in Python using NumPy:
```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of differential equations
def sys(t, z):
    x, y = z
    dxdt = -2*x + y
    dydt = -x - 2*y
    return [dxdt, dydt]
# Here we used a simple custom function. Pay attation to the formation and syntax since we should use it in further Object-Oriented Programming sections.

# Define the initial conditions
z0 = [1, 0]

# Set the time range to solve the system over
t_span = [0, 5]

# Solve the system of differential equations
sol = solve_ivp(sys, t_span, z0)

# Print the solution status
print(sol)

# Print the solution
print('t\t x(t)\t y(t)')
for t, x, y in zip(sol.t, sol.y[0], sol.y[1]):
    print('{:.2f}\t {:.4f}\t {:.4f}'.format(t, x, y))

# Plot the solution
plt.plot(sol.t, sol.y[0], label='x(t)')
plt.plot(sol.t, sol.y[1], label='y(t)')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Solution to the System of Differential Equations')
plt.show()
```
The output should be look like this:
```python 
# Status
  message: The solver successfully reached the end of the integration interval.
  success: True
   status: 0
        t: [ 0.000e+00  9.990e-04 ...  4.669e+00  5.000e+00]
        y: [[ 1.000e+00  9.980e-01 ... -3.661e-06  1.286e-05]
            [ 0.000e+00 -9.970e-04 ...  8.739e-05  4.324e-05]]
      sol: None
 t_events: None
 y_events: None
     nfev: 104
     njev: 0
      nlu: 0

  # Points over the time 
        
        t	 x(t)	 y(t)
0.00	 1.0000	 0.0000
0.00	 0.9980	 -0.0010
0.01	 0.9782	 -0.0107
0.11	 0.7962	 -0.0887
0.40	 0.4094	 -0.1752
0.74	 0.1676	 -0.1533
1.10	 0.0498	 -0.0984
1.50	 0.0037	 -0.0500
1.82	 -0.0065	 -0.0251
2.15	 -0.0074	 -0.0114
2.50	 -0.0054	 -0.0040
2.89	 -0.0030	 -0.0008
3.31	 -0.0013	 0.0002
3.73	 -0.0005	 0.0003
4.17	 -0.0001	 0.0002
4.67	 -0.0000	 0.0001
5.00	 0.0000	 0.0000

  # Graph:
  ...
```


