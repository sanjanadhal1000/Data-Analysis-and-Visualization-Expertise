# Dataset of weights: [60, 62, 58, 63, 61, 59]
# Find the 90% CI and 99% CI.

import numpy as np
from scipy import stats

data = np.array([60, 62, 58, 63, 61, 59])

mean = np.mean(data)
sd = np.std(data, ddof=1)
n = len(data)

se = sd/(np.sqrt(n))

# To calculate PPF input, t alpha/2, df -> alpha = 1 - CI, alpha/2 = area in each tail (as CI is two-sided).
# PPF input = 1 - (alpha/2)
t_crit_90 = stats.t.ppf(0.95, df=n-1)
t_crit_99 = stats.t.ppf(0.995, df=n-1)

margin_90 = t_crit_90 * se
margin_99 = t_crit_99 * se

CI_lower_90 = mean - margin_90
CI_upper_90 = mean + margin_90

CI_lower_99 = mean - margin_99
CI_upper_99 = mean + margin_99

print(f"Mean: {mean:.2f}")
print(f"\n90% Confidence Interval: {CI_lower_90:.2f}, {CI_upper_90:.2f}")
print(f"\n99% Confidence Interval: {CI_lower_99:.2f}, {CI_upper_99:.2f}")