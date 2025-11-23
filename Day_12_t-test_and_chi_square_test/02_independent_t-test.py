# Used to compare the mean of two independent groups.
# Example: A researcher wants to test whether male and female students have different average marks.

from scipy.stats import ttest_ind

group_A = [90,89,87,65,79]  # Marks of group A
group_B = [99,100,92,54,70] # Marks of group B

H0 = "μA = μB (Male and Female students have same average marks)"
H1 = "μA != μB (Male and Female students have different average marks)"

t_stat, p_value = ttest_ind(group_A, group_B)

print("Null Hypothesis (H0):",H0)
print("\nAlternative Hypothesis (H1):",H1)

print(f"\nt-Statistic: {t_stat:.2f}")
print(f"\np-value: {p_value:.2f}")

if p_value<=0.05:
    print("\nDecision: Reject H0 -> Means differ significantly")
else:
    print("\nDecision: Failed to reject H0 -> Means do not differ significantly")

