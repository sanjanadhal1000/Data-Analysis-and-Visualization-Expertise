'''
Task 1 — One-sample t-test

    A gym claims that average weight loss after 1 month = 5 kg.

    You have the sample data:

        import numpy as np
        import scipy.stats as stats

        data = np.array([4.8, 5.2, 4.4, 6.0, 5.1, 4.9, 5.3, 4.7, 5.5])

    Your work:

        Write H₀ and H₁

        Perform one-sample t-test:

            stats.ttest_1samp(data, popmean=5)


    Print p-value

    Decide whether to reject H₀ at α = 0.05

'''

import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_1samp

data = np.array([4.8, 5.2, 4.4, 6.0, 5.1, 4.9, 5.3, 4.7, 5.5])

H0 = "μ = 5kg"                                  # Avg. wt. loss after one month = 5kg.
H1 = "μ != 5kg"                                 # Avg. wt. loss after one month is not equal to 5kg.

result = stats.ttest_1samp(data, popmean=5)
p_value = result.pvalue                         # extract only p-value

print(f"Null Hypothesis: {H0}")
print(f"\nAlternative Hypothesis: {H1}")

print(f"\nTest Statistic: {result.statistic:.3f}")
print(f"\np-value: {p_value:.3f}")

alpha = 0.05

if p_value <= alpha:
    print(f"Decision: Reject H0 = {H0} at α = 0.05")
else:
    print(f"Decision: Failed to reject H0 = {H0} at α = 0.05")

