'''
Check if Car Color Preference Depends on Age Group.

| Age Group | Red | Blue | White |
| --------- | --- | ---- | ----- |
| 18–30     | 25  | 30   | 20    |
| 31–50     | 20  | 25   | 35    |

📌 Task:

Construct hypotheses

Run chi-square

Interpret

'''

import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [25,30,20],
    [20,25,35]
])

H0 = "Car Color Preference Does Not Depend on Age Group"
H1 = "Car Color Preference Depends on Age Group"

chi2, p_value, dof, expected_freq = chi2_contingency(table)

print(f"Chi-square value: {chi2:.2f}")
print(f"\np-value: {p_value:.2f}")
print(f"\nDegree of Freedom: {dof:.2f}")
print(f"\nExpected Frequencies: {expected_freq}")

if p_value<=0.05:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nDecision: Failed to reject H0 -> {H1}")