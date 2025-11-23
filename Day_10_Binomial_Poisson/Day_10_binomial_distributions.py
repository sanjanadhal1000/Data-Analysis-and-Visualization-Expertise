# Binomial Code + Plot

import numpy as np
import matplotlib.pyplot as plt

# Generate Binomial Distribution Data.
n = 10                           # No. of trials.
p = 0.5                          # Probability of Success.
size = 1000                      # No. of Samples.

binom_data = np.random.binomial(n,p,size)

# Plot Histogram.
plt.figure(figsize=(10,6))
plt.hist(binom_data, bins=range(0, n+2), density=True, alpha=0.7)
plt.title("Binomial Distribution (p = 0.5, n = 10)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()
