# Compute 95% CI

import numpy as np
from scipy import stats # SciPy stats for statistical functions (t-distribution).

data = np.array([52, 55, 50, 53, 54, 56]) # for easy maths operation.

# Sample Statistics
m = np.mean(data)
s = np.std(data,ddof=1) # ddof = 1 -> sample standard deviation, not population. 
# ddof -> Delta degrees of freedom -> Changes the denominator used when computing std dev
# ddof = 1 -> Variance shrinks slightly when estimating the mean from same sample. So divide by n-1 to correct the bias.
# Population data -> denominator = n, Sample std dev data -> den = n-1 (Bessel's Correction).
# Without ddof = 1, CI is incorrect and too small.
n = len(data)           # Sample Size

# Standard Error - measures the accuracy of the sample mean.
se = s/(n**0.5)

# t-critical value for 95% interval
t_crit = stats.t.ppf(0.975, df=n-1) # find the t-value such that 97.5% of t-distribution lies below it.
# df = degree of freedom -> how many values are free to vary.
# df=n-1 -> t-distribution compensates for uncertainty while calculating mean and std dev. As std dev uses n-1, df = n-1
# ppf -> percent point function -> Inverse of cumulative probability

# 0.975 is used as 95% CI splits the remaining 5% equally:
    # lower tail: 2.5%
    # upper tail: 97.5%
# So, we use t0.975 with df = n-1

# margin of error
margin = t_crit * se

# CI
CI_lower = m - margin
CI_upper = m + margin

print(f"Mean: {m:.2f}")
print(f"\n95% Confidence Interval: {CI_lower:.2f},{CI_upper:.2f}")

# Using Scipy's shortcut

# stats.t.interval(alpha=0.95, df=n-1, loc=mean, scale=se) # Returns the lower and upper bounds of CI using t-distribution.

'''
alpha=0.95: Confidence level. 95% CI -> middle 95% area under t-distribution. Remaining 5% split into 2.5% on each tail.

df = n-1: For one sample mean, df = n-1 always because:
    > when estimating a population mean using sample mean, we lose 1 df.
    > Ensures correct shape of t-distribution.

loc = mean: loc sets the center of t-distribution. For CI of mean, we use loc=mean.

scale=se : scale is the standard error of mean. Controls width of CI.

Returns a tuple (lower_limit,upper_limit).

Here, we use t and not z, because: 
    > n < 30
    > Unknown population std dev.
    > t-distribution has heavier tails and more conservative.

'''

