## The problem:

Suppose you have a cup of hot coffee, and you want to know how its temperature changes over time as it cools down to room temperature. The rate at which the coffee cools down depends on various factors such as the initial temperature, the ambient temperature, and the properties of the coffee cup.

We can model the temperature of the coffee as a function of time using the following differential equation:

```python

dT/dt = -k*(T - Ta)

```

where `T` is the temperature of the coffee, Ta is the ambient temperature (in this case, we'll assume it's 20 degrees Celsius), and `k` is a constant that depends on the properties of the coffee cup. We'll assume that `k = 0.1` for this example.

To solve this differential equation numerically, we'll use the solve_ivp function provided by the Scipy library. Here's the code:

```python
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

# For showing Solutions:
for t, T in zip(sol.t, sol.y[0]):
    print(f"Time: {t:.1f} s, Temperature: {T:.1f} C")

# Plot the solution
plt.plot(sol.t, sol.y[0], label='Coffee Temperature')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()
```

The solve_ivp function takes three arguments: the differential equation to solve (coffee_cooling), the time range to solve the equation over (`tspan`), and the initial condition (`[T0]`, which specifies the initial temperature of the coffee).

The output of `solve_ivp` is a `scipy.integrate.OdeResult` object that contains the solution to the differential equation. We can plot the temperature of the coffee as a function of time using the plot function from the Matplotlib library.

Here's the graph that shows the temperature of the coffee over time:
```
Time: 0.0 s, Temperature: 90.0 C
Time: 0.2 s, Temperature: 88.8 C
Time: 1.8 s, Temperature: 78.3 C
Time: 11.6 s, Temperature: 42.0 C
Time: 20.8 s, Temperature: 28.7 C
Time: 30.8 s, Temperature: 23.2 C
Time: 41.9 s, Temperature: 21.1 C
Time: 54.7 s, Temperature: 20.3 C
Time: 70.2 s, Temperature: 20.1 C
Time: 89.8 s, Temperature: 20.0 C
Time: 115.5 s, Temperature: 20.0 C
Time: 150.7 s, Temperature: 20.0 C
Time: 189.4 s, Temperature: 20.0 C
Time: 222.0 s, Temperature: 20.0 C
Time: 254.5 s, Temperature: 20.0 C
Time: 288.7 s, Temperature: 20.0 C
Time: 323.3 s, Temperature: 20.0 C
Time: 356.5 s, Temperature: 20.0 C
Time: 388.0 s, Temperature: 20.0 C
Time: 419.7 s, Temperature: 20.0 C
Time: 453.3 s, Temperature: 20.0 C
Time: 488.2 s, Temperature: 20.0 C
Time: 522.3 s, Temperature: 20.0 C
Time: 554.3 s, Temperature: 20.0 C
Time: 585.4 s, Temperature: 20.0 C
Time: 618.0 s, Temperature: 20.0 C
Time: 652.7 s, Temperature: 20.0 C
Time: 687.6 s, Temperature: 20.0 C
Time: 720.5 s, Temperature: 20.0 C
Time: 751.6 s, Temperature: 20.0 C
Time: 783.2 s, Temperature: 20.0 C
Time: 817.0 s, Temperature: 20.0 C
Time: 852.4 s, Temperature: 20.0 C
Time: 886.6 s, Temperature: 20.0 C
Time: 918.1 s, Temperature: 20.0 C
Time: 948.9 s, Temperature: 20.0 C
Time: 981.6 s, Temperature: 20.0 C
Time: 1016.8 s, Temperature: 20.0 C
Time: 1052.1 s, Temperature: 20.0 C
Time: 1084.7 s, Temperature: 20.0 C
Time: 1115.2 s, Temperature: 20.0 C
Time: 1146.6 s, Temperature: 20.0 C
Time: 1180.9 s, Temperature: 20.0 C
Time: 1200.0 s, Temperature: 20.0 C
```
and the graph would be:

![image](https://user-images.githubusercontent.com/109058050/228893988-ea5ae827-1b6d-4396-9ac8-655e7bb4ec6d.png)

As we can see from the graph, the temperature of the coffee decreases exponentially over time, eventually approaching the ambient temperature of 20 degrees Celsius. This behavior is consistent with the differential equation we used to model the system.
