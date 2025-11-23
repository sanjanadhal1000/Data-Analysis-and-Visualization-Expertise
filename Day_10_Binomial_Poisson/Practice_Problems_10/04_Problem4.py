# Compare how Binomial and Poisson look when n is large & p small.

import numpy as np
import matplotlib.pyplot as plt

n = 20000
p = 0.1
size = 1000
lam = 4

binom_data = np.random.binomial(n,p,size)
poisson_data = np.random.poisson(lam, size)

plt.figure(figsize=(8,6))
plt.hist(binom_data, bins=range(0,(n+2)), density=True, alpha=0.7)
plt.title("Binomial Distribution (n=large, p=small)")
plt.xlabel("No. of Successes")
plt.ylabel("Probability")
plt.show()

plt.figure(figsize=(8,6))
plt.hist(poisson_data, bins=range(0,(max(poisson_data)+2)), density=True, alpha=0.7)
plt.title("Poisson Distribution (n=large, p=small)")
plt.xlabel("No. of Events")
plt.ylabel("Probability")
plt.show()

# For binomial distribution, check its plot in problem_4_plot.png
# For poisson, it will show an error, as poisson distribution takes lambda as the argument, not n or p.