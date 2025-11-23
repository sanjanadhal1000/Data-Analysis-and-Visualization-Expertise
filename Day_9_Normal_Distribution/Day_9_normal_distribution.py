# Generate Normal Distribution Data.

import numpy as np
import random
import matplotlib.pyplot as plt

# Mean and Std. Dev.
m = 50
sd = 10

# Generate 1000 random values following a normal distribution.
data = np.random.normal(m,sd,1000)

print(f"Mean of Data: {np.mean(data):.2f}. \nStandard Deviation of Data: {np.std(data):.2f}.")

# Visualize the Normal Distribution - Plot a Histogram + Intensity Curve.
plt.figure(figsize=(8,5))

plt.hist(data, bins=30, density=True)

plt.title("Normal Distribution (Mean = 50 and Standard Deviation = 10)")
plt.xlabel("Value")
plt.ylabel("Density")

plt.show()

# Mean ± Sigma Shading (Optional Upgrade)
# This version visually shows the 68–95–99.7 rule.
mu = np.mean(data) # Mean - Average Value of dataset.
sigma = np.std(data) # Standard Deviation - how spread out the values are. 

# We want to draw vertical lines at:

# Mean

# Mean - 1σ

# Mean + 1σ

plt.figure(figsize=(8,6)) # 8 inches wide and 6 inches tall. 
# To make the plot easier to read and more visually balanced.

count,bins,_ = plt.hist(data,bins=30,density=True,alpha=0.6) 
# bins=30 - divides the data into 30 equal sections.
# density=True - Shows probability density instead of raw counts.
# alpha=0.6 - Gives the bars 60% opacity (slightly transparent).
# Histogram visualizes the shape of the normal distribution.
# count - heights of the bars.
# bins - boundaries of each bins.
# _ - ignores the third returned object (histogram patches).

# mean line
plt.axvline(mu,color="black",linestyle="--",label="Mean") 
# Visually show the center of the distribution.
# Draw vertical line at the mean.
# axvline - draw a vertical line.
# -- - dashed line
# label="Mean" - Add label "Mean" to show in the legend.

# 1 - Sigma
plt.axvline(mu - sigma,color="blue",linestyle="--",label="Mean - 1σ") 
# Draws a vertical line at one standard deviation to the left of the mean.
# Shows the start of the 68% range in ND.

plt.axvline(mu + sigma,color="green",linestyle="--",label="Mean + 1σ")
# Draws a vertical line at one SD to the right of the mean

plt.title("Normal Distribution with Mean + 1σ")
plt.xlabel("Value")
plt.ylabel("Density") # Here, density refers to probability density.

plt.legend() 
# To show labels for Mean, Mean - 1σ, and Mean + 1σ.

plt.show()
