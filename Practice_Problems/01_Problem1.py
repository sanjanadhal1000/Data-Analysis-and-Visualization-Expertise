'''
Q1. A dice is rolled.

Find probability of:

A: getting a number > 4

B: getting an even number

A ∩ B: number > 4 and even

'''

S = [1,2,3,4,5,6]

A = [5,6]
B = [2,4,6]
A_inter_B = [6]

p_A = len(A)/len(S)
p_B = len(B)/len(S)
p_A_inter_B = len(A_inter_B)/len(S)

print(f"Probability of A (getting a number greater than 4): {p_A:.1f}. \nProbability of B (getting an even number): {p_B:.1f}. \nProbability of A intersection B: {p_A_inter_B:.1f}")
