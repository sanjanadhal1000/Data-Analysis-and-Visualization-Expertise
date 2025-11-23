'''
A school wants to test if boys and girls have different average math scores.

Scores:

Boys → [78, 82, 75, 80, 79, 77]

Girls → [85, 88, 84, 90, 87, 86]

📌 Task:

Write hypotheses

Run scipy.stats.ttest_ind()

Interpret results

'''
from scipy.stats import ttest_ind

marks_B = [78, 82, 75, 80, 79, 77]
marks_G = [85, 88, 84, 90, 87, 86]

H0 = "μB = μG (Boys and Girls have same average math scores)"
H1 = "μB != μG (Boys and Girls have different average math scores)"

t_stat, p_value = ttest_ind(marks_B,marks_G,equal_var=False)

print(f"t-Statistic: {t_stat:.2f}")
print(f"\np-value: {p_value:.2f}")

alpha = 0.05
if p_value<=alpha:
    print(f"\nDecision: Reject H0 -> {H0}")
else:
    print(f"\nFailed to reject H0 -> {H1}")
