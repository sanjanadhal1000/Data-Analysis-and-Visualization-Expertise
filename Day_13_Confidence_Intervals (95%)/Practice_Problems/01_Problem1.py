# Data: [10, 12, 9, 11, 13, 12]
# Compute 95% CI for the mean.

import numpy as np
from scipy import stats

data = np.array([10, 12, 9, 11, 13, 12])

mean = np.mean(data)
sd = np.std(data, ddof=1)
n = len(data)

se = sd/(np.sqrt(n))

t_crit = stats.t.ppf(0.975, df = n-1)

margin = t_crit * se

CI_lower = mean - margin
CI_upper = mean + margin

print(f"Mean: {mean:.2f}")
print(f"\nStandard Deviation: {sd:.2f}")
print(f"\nSample Size of Data: {n}")
print(f"\nStandard Error: {se:.2f}")
print(f"\nt-critical value: {t_crit:.2f}")
print(f"\nMargin value: {margin:.2f}")
print(f"\n95% Confidence Interval: {CI_lower:.2f}, {CI_upper:.2f}")