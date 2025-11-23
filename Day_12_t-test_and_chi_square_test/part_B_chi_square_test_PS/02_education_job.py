'''
Does Education Level Affect Job Satisfaction?

| Education | Satisfied | Not Satisfied |
| --------- | --------- | ------------- |
| Graduate  | 30        | 20            |
| Postgrad  | 40        | 10            |

📌 Task:

Write hypotheses

Run chi-square

Interpret

'''

import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [30,20],
    [40,10]
])

H0 = "Education level does not affect Job Satisfaction"
H1 = "Education level affects Job Satisfaction"

chi2, p_value, dof, expected_freq = chi2_contingency(table)

print(f"Chi-square Value: {chi2:.2f}")
print(f"\np-value: {p_value:.2f}")
print(f"\nDegree of Freedom: {dof:.2f}")
print(f"\nExpected Frequencies: {expected_freq}")

if p_value<=0.05:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nDecision: Failed to reject H0 -> {H1}")