# Calculate mean & variance of your Binomial and Poisson data.
# (Hint: np.mean() and np.var())

import numpy as np

n = 20
p = 0.3
size = 1000

binom_data = np.random.binomial(n,p,size)

binom_mean = np.mean(binom_data)
binom_variance = np.var(binom_data)

lam = 2.5
size = 1000

poisson_data = np.random.poisson(lam, size)

poisson_mean = np.mean(poisson_data)
poisson_variance = np.var(poisson_data)

print(f"Binomial Mean: {binom_mean:.2f} \nBinomial Variance: {binom_variance:.2f} \nPoisson Mean: {poisson_mean:.2f} \nPoisson Variance: {poisson_variance:.2f}")