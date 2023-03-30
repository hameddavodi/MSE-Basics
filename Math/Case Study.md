## The problem:

Suppose you have a cup of hot coffee, and you want to know how its temperature changes over time as it cools down to room temperature. The rate at which the coffee cools down depends on various factors such as the initial temperature, the ambient temperature, and the properties of the coffee cup.

We can model the temperature of the coffee as a function of time using the following differential equation:


'dT/dt = -k*(T - Ta)'

where T is the temperature of the coffee, Ta is the ambient temperature (in this case, we'll assume it's 20 degrees Celsius), and k is a constant that depends on the properties of the coffee cup. We'll assume that k = 0.1 for this example.

To solve this differential equation numerically, we'll use the solve_ivp function provided by the Scipy library. Here's the code:

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation
def coffee_cooling(t, T):
    k = 0.1
    Ta = 20
    return -k*(T - Ta)

# Define the initial temperature of the coffee and the time range
T0 = 90
tspan = [0, 1200]

# Solve the differential equation numerically
sol = solve_ivp(coffee_cooling, tspan, [T0])

# Plot the solution
plt.plot(sol.t, sol.y[0], label='Coffee Temperature')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()

'''
The solve_ivp function takes three arguments: the differential equation to solve (coffee_cooling), the time range to solve the equation over (tspan), and the initial condition ([T0], which specifies the initial temperature of the coffee).

The output of solve_ivp is a scipy.integrate.OdeResult object that contains the solution to the differential equation. We can plot the temperature of the coffee as a function of time using the plot function from the Matplotlib library.

Here's the graph that shows the temperature of the coffee over time:



As we can see from the graph, the temperature of the coffee decreases exponentially over time, eventually approaching the ambient temperature of 20 degrees Celsius. This behavior is consistent with the differential equation we used to model the system.
