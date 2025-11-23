'''
Association between Gender and Shopping Preference

| Gender | Online | Offline |
| ------ | ------ | ------- |
| Male   | 40     | 30      |
| Female | 50     | 20      |

📌 Task:

Write H₀: No association

Write H₁: Association

Use chi2_contingency()

Interpret

'''
import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [40,30],
    [50,20]
])

H0 = "No association"
H1 = "Association"

chi2, p_value, dof, expected_freq = chi2_contingency(table)

print(f"Chi-square value: {chi2:.2f}")
print(f"\np-value: {p_value:.2f}")
print(f"\nDegree of Freedom: {dof:.2f}")
print(f"\nExpected Frequencies: {expected_freq}")

if p_value<=0.05:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nDecision: Failed to reject H0 -> {H1}")