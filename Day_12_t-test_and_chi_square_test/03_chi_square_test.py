# Used to check association between categorical variables.
# Example problem: Is there a relationship between Gender (Male/Female) and Preference (Tea/Coffee)?

'''
Contingency Table:

|        | Tea | Coffee |
| ------ | --- | ------ |
| Male   | 30  | 20     |
| Female | 25  | 25     |

'''

import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [30,20],         # Male
    [25,25]          # Female
])

H0 = "No association between Gender and Preference"
H1 = "Association between Gender and Preference"

chi2, p_value, dof, expected_freq = chi2_contingency(table)

print(f"Chi-square value: {chi2:.2f}")
print(f"\np-value: {p_value:.2f}")
print(f"\nDegree of Freedom: {dof:.2f}")
print(f"\nExpected Frequency: {expected_freq}")

if p_value<=0.05:
    print(f"Decision: Reject H0 -> {H0}")
else:
    print(f"Decision: Failed to reject H0 -> {H1}")