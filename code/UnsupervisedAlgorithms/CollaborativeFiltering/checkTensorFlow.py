import tensorflow as tf

# Create the input features tensor
X = tf.constant([[1, 2], [3, 4]])

# Create the weights tensor
W = tf.constant([[5, 6], [7, 8]])

# Create the bias tensor
b = tf.constant([9, 10])

# Create the target values tensor
Y = tf.constant([[11, 12], [13, 14]])

# Create the R tensor indicating whether the input features are valid
R = tf.constant([[1, 0], [1, 1]])

lambda_ = 1.5

# Compute the prediction error
j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R

# Print the prediction error
print(j)

