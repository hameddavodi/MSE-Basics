
# To find probabilities in Python using NumPy, you can use the numpy.random module. 
# This module provides various functions for generating random numbers and distributions.

# In this example, we generated 1000 random numbers between 0 and 1 using the random() function from the numpy.random module. 
# Then, we counted the number of values that are greater than 0.5 using NumPy's sum() function. 
# Finally, we divided the count by the total number of data points to calculate the probability of the event occurring.

import numpy as np

# Generate 1000 random numbers between 0 and 1
data = np.random.random(1000)

# Count the number of values greater than 0.5
count = np.sum(data > 0.5)

# Calculate the probability of the event occurring
probability = count / len(data)

# Print the result
print("The probability of the event is:", probability)

# Output
The probability of the event is: 0.48



