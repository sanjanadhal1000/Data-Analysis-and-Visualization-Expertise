# The average study time from a sample of 20 students is 2.4 hours
# Sample std = 0.5 hours
# Compute 95% CI.

import numpy as np
from scipy import stats

mean = 2.4
sd = 0.5
n = 20

se = sd/np.sqrt(n)

t_crit = stats.t.ppf(0.975, df=n-1)

margin = t_crit * se

CI_lower = mean - margin
CI_upper = mean + margin

print(f"95% CI: {CI_lower:.2f} hours, {CI_upper:.2f} hours")