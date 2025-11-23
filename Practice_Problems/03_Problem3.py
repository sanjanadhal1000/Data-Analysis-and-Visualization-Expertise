'''
Q3. How many 4-digit numbers can be made using digits 1–9 without repetition?

'''
# Permutation - We have 9 digits (1-9) and we want 4 digit numbers.
# So, 9P4 = 9*8*7*6 = 3024

import math

count = math.perm(9,4)
print("Total 4-digit numbers: ",count)

