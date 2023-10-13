import matplotlib.pyplot as plt
import numpy as np

# Assume X is your data
X = np.random.rand(10, 2)  # Example data

plt.plot(X[:,0], X[:,1], 'ro')
plt.show()  # This will display the plot
