import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from pca_utils import plot_widget
import matplotlib.pyplot as plt
import plotly.offline as py
from bokeh.io import show
from bokeh.io import output_notebook
from bokeh.plotting import figure

# py.init_notebook_mode()
# output_notebook()

X = np.array([[ 99,  -1],
       [ 98,  -1],
       [ 97,  -2],
       [101,   1],
       [102,   1],
       [103,   2]])

plt.plot(X[:,0], X[:,1], 'ro')
plt.show()  # This will display the plot

# Loading the PCA algorithm
pca_2 = PCA(n_components=1)
# pca_2

# Let's fit the data. We do not need to scale it, since sklearn's implementation already handles it.
pca_2.fit(X)

print(pca_2.explained_variance_ratio_)

X_trans_2 = pca_2.transform(X)
print(X_trans_2)

# Let's plot the transformed data
x_coords = np.zeros_like(X_trans_2)  # creates a new array with the same shape as X, filled with zeros
y_coords = X[:, 0]  # extracts the values from X

plt.scatter(x_coords, y_coords)  # creates a scatter plot
plt.show()  # displays the plot

