
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

# To generate probability distributions in Python using NumPy, you can use the numpy.random module. 
# The example of discrete probability distribution (Poisson)

import numpy as np
import matplotlib.pyplot as plt

# set the lambda parameter
lam = 5

# generate 1000 samples from the Poisson distribution
samples = np.random.poisson(lam, size=1000)

# calculate the CDF
counts, bin_edges = np.histogram(samples, bins=np.arange(0, max(samples)+1))
cdf = np.cumsum(counts) / sum(counts)

# print CDF and PDF
print(samples)
print(cdf)

# Output
the PDF sample is: 
[ 2  1  5  7  6  4  5  5  6 11  8  7  5  7  4  4  4  6  4  2  4  9  6  6
  6  6  4  4  5  7  7 12  9  2  2  6  6  5  2  9  5  6  7  2  7  5  3  4
  3  2  7  4  6  7  4  8  6  5  9  1  6  0  2  5 11  5  5  5  6  8  4  4
  3  3  5  8  8  4  8  3  8  9  2  3  2  5  6  6  6  6  5  6  8  5  8  7
  9  9  1  4  3  3  6  5  3  7  5  3  6  5  3  7  4  7  5  6  9  3  4  5
  5  5  3  5  1  4  6  7  6  7  1  3  8  6  4  5  3  5  7  6  7  6  8  2
  4  6  5  3  2  4  2  3  7  5  4  7  8  2  2  6  3  3  5  6  5  6 11  7
  8  5  6  4  5  3  5  3  4  7  4  6  2  3  6  7  6  2  6  8  9  5  4  3
  3  6  5  7  5  4  5  4  6  2  4  9  3  7  5 11  7  3  3  7  5  4  2  5
  7  5  5  6  6  2  3  1  4  6  4  7  1  6  7  6  5  7  4 10  5  8  7  5
  5  5  4  5  5  2  5  4  2  2  5  5  4  6  4  6  0  8  3  3  3  4  9  7
  5  3  3  1  4  6  6  3  4  3  5  6  5  4  4  7  4  3  3  4  7  2  2  3
  3  2  7  7  3  4  6  8  5  3  3  5  3  8  6  5  5  5  9  5  4  3  3  4
  8  7  5  5  0  2  6  5  3  3  5  9  5  5  5  3  6  6  5  5  7  7  8  3
  5  4  4  5  6  4  5  4  2  8  7  5  1  6  4  3  8  5  7  6  9  3  6 10
  4  2 10  3  4  7  7  4  5  7  7  4  7  9  5  5  8  2  5  5  3  7  8  5
  3  2  7  3  1  7  3  6  8  9  5  6  5  6  7  5  1  7  3  6  1  7  8  8
  6  4  4  8  5  6  5  6  4  4  5  4  7  6  9  3  5  3  4  3  5  6  3  5
  4  4  5  6  6  1  3  5  8  9  8  8  5  2  6  7  6  8  8  4  5  6  7  5
  4  5  5  7  7  7  3  8  4  3  8  7  3  6  4  4  4  4  5 10  2  7  9  5
 10  6  2  2  8  3  2  9  6  3  5  3  4  9  7  9  4  6  3  9  3  9  2  5
  6  4  3  6  4  9  6  2  4  7  4  7  5  6  9  7  6  5  7  3  5  4  6  6
  3  4  3  3  3  2  5  7  1  5  1  7  5  6  7  4  3  5  5  6  2  4  7  5
  3  3  1  6  9  5  4  5  4  6  2  7  8  2  6  7  4  4  6  4  4  4  3  4
  6  1  4  5  5  5  3  7  6  4  2  2  2  5  3  8  4  7  7  4  5  4  4  3
  4  9  4  2  5  4  4  8  4  3  6  7  5 11  5  3  6  6  5  5  5  4  6  6
  2  6  6  4 10  5  5  6  2  2  9  8  9  7  6  4 12  3  4  3  6  6  6  4
  4  3  6  6  2 11  5  3 13  6  6  3  1  2  7  6  5  5  7  5 12  6  2  4
  4  7  8  2  5  8  5  4  2  4  6  2  3  3  1  7  3  6  7  5  4  5  6  3
  3  3  3  4  4  7 11 10  4  4  2  6  4  3  5  5  7  7  3 10  2  2  3  2
  7  2  5  2  2  9  8  7  4  4  2  5  1  6  6  4  4  8  5  2  2  4  7  6
  2  4  8  8  6  8  8  5  4  7  6  5  5  4  5  4  6  1  4  6  6  1  7  3
  8  6  4  4  5 11  3  2  4  5  4  6  6  5  8  8  8  2 10  4  6  6  5  3
  7  5  4  5  3  7  7  1  2  6  6  6  6  5  3  2  6  7  0  5  1  5  2  7
  5  3  6  7  3  3  6  2  4  9  4  7  5  2  5  7  5  6  4  6  3  5  5  9
  6  5  5  5  8  5  4  5  5  6  4  3  7  7  3  7  3  3  5  5  6  2  4  4
  4  4  7  3  8  5  5  7  2  2  2  5  5  2  6  5  4  7  6  3  5  6  6  7
  2  5  5  3  6  5  1  5  5  3  8  3  7  4  5  6 12  9  2  5  3  3  4  6
  8  2  5  2  4  1  7  7  2  7  2  3  9  7  5  6  7  7  7  4  8  4  1  2
  8  4  4  5  5  4  5  3  4  5  4  3  6  5 10  6  4  6  2  6  6  4  5  4
  6  9  5  5  5  3  6  3  7  6  2  1  3  6  3  6  6  8  3  4  4  4  2  4
  4  5  6  9  4  7  6  5  4  8  6  8  7  4  4  3]
  
the CDF would be: [0.004 0.032 0.12  0.249 0.413 0.605 0.764 0.879 0.94  0.977 0.987 0.995  1.   ]

# In the code above, we set the lambda parameter to 5 for the Poisson distribution. 
# We then generate 1000 samples from the Poisson distribution using the numpy.random.poisson() function, and store them in the samples array. 
# Finally, we calculate the CDF by computing the histogram of the samples and then cumulatively summing the counts. 


# The example of continuous probability distribution (Gamma)
import numpy as np

# set the shape and scale parameters
shape = 2.0
scale = 1.5

# generate 1000 samples from the gamma distribution
samples = np.random.gamma(shape, scale, size=1000)

# print the first 10 samples
print(samples[:10])

# Output
[3.08334738 2.02618989 1.80632048 0.24750669 1.8644953  2.74282052
 3.87019445 4.0711554  4.24655067 4.36236416]




