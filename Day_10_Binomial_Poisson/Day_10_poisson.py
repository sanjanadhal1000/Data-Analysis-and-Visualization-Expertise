# Poisson Distribution + Plot

import numpy as np
import matplotlib.pyplot as plt

lam = 4 # Average rate or lambda.
size = 1000 # No. of samples.

poisson_data = np.random.poisson(lam, size)

plt.figure(figsize=(10,6))
plt.hist(poisson_data, bins = range(0, max(poisson_data)+2), density=True, alpha=0.7)
plt.title("Poisson Distribution (lambda = 4)")
plt.xlabel("No. of Events")
plt.ylabel("Probability")
plt.show()