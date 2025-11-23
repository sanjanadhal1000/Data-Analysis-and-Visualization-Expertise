'''
Task 2 — Two-sample t-test (Independent)

    Two trainers use different workout plans. You want to check if their results differ.

        group_A = np.array([52, 55, 50, 53, 54, 56])
        group_B = np.array([48, 51, 49, 50, 52, 47])

Your work:

    Hypotheses

    Perform:

        stats.ttest_ind(group_A, group_B, equal_var=False)


    Interpret results

'''

import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_ind

group_A = np.array([52, 55, 50, 53, 54, 56])
group_B = np.array([48, 51, 49, 50, 52, 47])

H0 = "μ (group-A) = μ (group-B) -> Workout plans of Group A and Group B does not differ"
H1 = "μ (group-A) != μ (group-B) -> Workout plans of Group A and Group B differ"

result = stats.ttest_ind(group_A, group_B, equal_var=False)
t_stat = result.statistic
p_value = result.pvalue

print(f"Null Hypothesis: {H0}")
print(f"\nAlternative Hypothesis: {H1}")
print(f"\nt-statistic value: {t_stat:.3f}")
print(f"\np-value: {p_value:.3f}")

alpha = 0.05

if p_value <= alpha:
    print("Decision: Reject H0 -> Workout plans differ significantly.")
else:
    print("Decision: Failed to reject H0 -> Workout plans don't differ significantly.")

