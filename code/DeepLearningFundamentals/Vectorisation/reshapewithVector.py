import numpy as np

# Assuming X is a 4D array with dimensions 10x8x8x3
X = np.random.rand(5, 8, 8, 3)

print("x shape", X.shape)
sample_data = X[0]

print("sample_data ", sample_data)

# Reshape and transpose the 4D array
X_flatten = X.reshape(X.shape[0], -1).T
sample_flatten = X_flatten[0]

print("x_flatten shape", X_flatten.shape)

print("sample_flatten ", sample_flatten)