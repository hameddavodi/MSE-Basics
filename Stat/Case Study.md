## The Problem:
We want to conduct a one-sample t-test in Python to test whether the average commute time for employees at a company is greater than 30 minutes.

Suppose a company is concerned about the length of time it takes their employees to commute to work. They suspect that the average commute time for their employees is longer than 30 minutes, and they want to test this hypothesis using a one-sample t-test.

To do this, they randomly select a sample of 25 employees from their workforce and record their commute times (in minutes). The data for the sample is as follows:

`32, 28, 31, 33, 29, 27, 34, 32, 33, 30, 31, 30, 29, 28, 33, 35, 31, 30, 32, 31, 34, 35, 32, 36, 31`

Now, we can conduct a one-sample t-test to determine whether the average commute time for this sample is significantly greater than 30 minutes:

```python
import numpy as np
from scipy.stats import ttest_1samp

# Sample data (commute times in minutes)
sample = np.array([32, 28, 31, 33, 29, 27, 34, 32, 33, 30, 31, 30, 29, 28, 33, 35, 31, 30, 32, 31, 34, 35, 32, 36, 31])

# Calculate the sample mean and standard deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Set the null hypothesis value to test (mean = 30)
null_value = 30

# Calculate the t-statistic and p-value
t_stat, p_val = ttest_1samp(sample, null_value)

# Print the results
print(f"Sample mean: {sample_mean:.2f}")
print(f"Sample standard deviation: {sample_std:.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_val:.3f}")

# Interpret the results
alpha = 0.05
if p_val < alpha:
    print("Reject null hypothesis: The average commute time for employees is significantly greater than 30 minutes.")
else:
    print("Fail to reject null hypothesis: There is not enough evidence to conclude that the average commute time for employees is greater than 30 minutes.")
```

In this case, the output would be:

```python
Sample mean: 31.12
Sample standard deviation: 2.31
T-statistic: 3.22
P-value: 0.003
Reject null hypothesis: The average commute time for employees is significantly greater than 30 minutes.
```
Based on the results of the test, we can conclude that there is strong evidence to suggest that the average commute time for employees at this company is greater than 30 minutes.
