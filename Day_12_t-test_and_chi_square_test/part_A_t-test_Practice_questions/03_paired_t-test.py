'''
A fitness trainer wants to know if a new diet plan causes weight reduction.

Weights Before: [72, 75, 80, 85, 78, 82]
Weights After: [70, 73, 77, 82, 76, 80]

📌 Task:

Write H₀ and H₁

Use scipy.stats.ttest_rel(before, after)

Interpret

'''

from scipy.stats import ttest_rel

before = [72, 75, 80, 85, 78, 82]
after = [70, 73, 77, 82, 76, 80]

H0 = "The new diet plan doesn't cause weight reduction"
H1 = "The new diet plan causes weight reduction"

t_stat, p_value = ttest_rel(before, after)

print(f"t-Statistic: {t_stat:.2f}")
print(f"\np-value: {p_value:.2f}")

alpha = 0.05
if p_value<=alpha:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nDecision: Failed to reject H0 -> {H1}")

