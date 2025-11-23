'''
Q4. Simulate 500 dice rolls using NumPy and find frequency of each number.

'''

import numpy as np
import random

rolls = np.random.randint(1,7,size=500)

unique, counts = np.unique(rolls, return_counts=True)

# Convert NumPy ints to normal Python ints for clean printing
freq = {int(k) : int(v) for k, v in zip(unique, counts)}

print("Frequency:\n")
print(freq)