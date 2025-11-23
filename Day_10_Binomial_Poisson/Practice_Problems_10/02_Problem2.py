# Generate Poisson (λ=2.5) and plot.

import numpy as np
import matplotlib.pyplot as plt

lam = 2.5
size = 1000

poisson_data = np.random.poisson(lam, size)

plt.figure(figsize=(8,6))
plt.hist(poisson_data, bins=range(0,(max(poisson_data)+2)), density=True, alpha=0.5)
plt.title("Poisson Distribution (lambda=2.5)")
plt.xlabel("No. of Events")
plt.ylabel("Probability")
plt.show()