'''
A company claims the average battery life of their headphones is 20 hours.
A sample of 12 devices gives the following lifetimes:

[18, 22, 19, 20, 21, 23, 19, 20, 18, 22, 21, 20]

📌 Task:

State H₀ and H₁

Perform one-sample t-test

Interpret p-value

'''
from scipy.stats import ttest_1samp

sample = [18, 22, 19, 20, 21, 23, 19, 20, 18, 22, 21, 20]

H0 = "μ = 20 (Average battery life of their headphones is 20 hours)"
H1 = "μ != 20 (Average battery life of their headphones is not equal to 20 hours)"

t_stat, p_value = ttest_1samp(sample, popmean=20)

print(f"t-statistic: {t_stat:.2f}")
print(f"\np-value: {p_value:.2f}")

alpha=0.05
if p_value<=alpha:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nDecision: Failed to reject H0 -> {H1}")





