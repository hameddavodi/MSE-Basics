## Dataset Types:
    Cross-sectional data: A single snapshot of data collected at a specific point in time, where each observation represents a different individual or entity.
    Time series data: Data collected over a period of time, often at regular intervals, where each observation represents a different point in time.
    Panel data: A combination of cross-sectional and time series data, where multiple observations are collected for the same individuals or entities over time.
    Longitudinal data: Similar to panel data, but with a focus on the same individuals or entities being observed and measured repeatedly over a longer period of time.
    Pooled data: A combination of data from multiple sources or studies, often used for meta-analyses or to increase the sample size of a study.
To import data in Python with NumPy, you can use the loadtxt() function. Here's an example of how to use it:
```python
import numpy as np
data = np.loadtxt('filename.txt')
```
You can also specify additional parameters, such as the delimiter (if it's not a standard space or comma) or which columns to load.

```python
data = np.loadtxt('filename.csv', delimiter=';', skiprows=1)
```
There is a specific function for numpy `np.description` gives us an overal summary about the data:

```python
# Get summary statistics
summary = np.describe(data)
```
This will output the summary statistics for the data in a formatted manner. You can also access individual summary statistics by using the following attributes:
```python
    summary.min
    summary.max
    summary.mean
    summary.std
    summary.count
    summary.percentiles
```
These attributes can be useful if you need to access specific statistics for further analysis or modeling.
