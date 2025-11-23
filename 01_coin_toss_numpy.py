# Simulate 10 coin tosses.

import numpy as np
import random

tosses = np.random.choice(['H','T'], size=10)
print(tosses)

# Simulate 1000 tosses and calculate probability.

toss = np.random.choice(['H','T'], size = 1000)

p_heads = np.mean(toss=='H')
p_tails = np.mean(toss=='T')

print("Probability of Heads(H): ",p_heads)
print("Probability of Tails(T): ",p_tails)

# Simulate Multiple Experiments.

experiments = 10000
heads_count = np.sum(np.random.choice(['H','T'], size = experiments)=='H')

print("Experimental Probability of Heads: ",heads_count/experiments)