'''
Task 3 — Proportion z-test

    A website claims conversion rate = 15%.

    In a new experiment:

        200 people visited

        40 clicked the button


    Check if conversion > 15%.

Your work:

    H₀ and H₁

    Compute sample proportion p̂ = 40/200

    Use:

        from statsmodels.stats.proportion import proportions_ztest

    count = 40
    nobs = 200
    value = 0.15

    proportions_ztest(count, nobs, value, alternative='larger')


Print p-value, conclusion.

'''
import numpy as np
# import scipy.stats as stats
# from scipy.stats import ztest
from statsmodels.stats.proportion import proportions_ztest

count = 40 # no. of clicks
nobs = 200 # total visitors
value = 0.15 # claimed conversion rate

z_stat, p_value = proportions_ztest(count, nobs, value, alternative='larger')

H0 = "p = 0.15 (Conversion rate = 15%)"
H1 = "p > 0.15 (Conversion rate is greater than 15%)"

print(f"Null Hypothesis: {H0}")
print(f"\nAlternative Hypothesis: {H1}")
print(f"\nZ-statistic value: {z_stat:.3f}")
print(f"\np-value: {p_value:.4f}")

alpha = 0.05

if p_value<=alpha:
    print("\nDecision: Reject H0 -> Conversion rate is greater than 15%")
else:
    print("\nDecision: Failed to reject H0 -> Conversion rate is 15%")




