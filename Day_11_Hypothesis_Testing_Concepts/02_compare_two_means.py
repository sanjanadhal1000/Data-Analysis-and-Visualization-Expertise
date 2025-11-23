# Do two restaurant branches have different average ratings?

# Step 1: Hypotheses
'''
H₀: μ₁ = μ₂
Ha: μ₁ ≠ μ₂

'''

# Use Independent t-test
import scipy
from scipy.stats import ttest_ind 

# ttest_ind - performs an independent two-sample t-test.
# Use it to compare means of two different independent groups.

branch1 = [4.2, 3.0, 4.8, 5.0, 4.9]
branch2 = [4.4, 3.3, 4.7, 2.0, 1.9]

# Main hypothesis test
t_stat,p_value = ttest_ind(branch1,branch2)

# Compares the mean of branch 1 vs branch 2.
# t_stat - t-statistic value (measures how far apart the sample means are, in terms of standard error).
# Larger |t| - More difference b/w groups.
# p_value - probability of observing this difference if the null hypothesis H0 were true.
# if p < 0.05 - groups differ significantly.

print(f"t-static: {t_stat:.1f}")
print(f"p-value: {p_value:.1f}")

# if p < 0.05 => significant difference
# if p > 0.05 => no significant difference