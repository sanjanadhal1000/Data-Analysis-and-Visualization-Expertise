# Generate Binomial (n=20, p=0.3) and plot.

import numpy as np
import matplotlib.pyplot as plt

n = 20
p = 0.3
size = 1000

binom_data = np.random.binomial(n, p, size)

plt.figure(figsize=(10,6))
plt.hist(binom_data, bins = range(0,(n+2)), density = True, alpha=0.6)
plt.title("Binomial Distribution (n=20, p=0.3)")
plt.xlabel("No. of Successes")
plt.ylabel("Probability")
plt.show()

