import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate data from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Create a Q-Q plot
sm.qqplot(data, line='45')
plt.title('Q-Q Plot of Normally Distributed Data')
plt.show()