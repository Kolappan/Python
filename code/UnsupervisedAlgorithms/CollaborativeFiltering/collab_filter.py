import numpy as np
import tensorflow as tf
from tensorflow import keras
from recsys_utils import *

#Load data
X, W, b, num_movies, num_features, num_users = load_precalc_params_small()
Y, R = load_ratings_small()

print("Y", Y.shape, "R", R.shape)
print("X", X.shape)
print("W", W.shape)
print("b", b.shape)
print("num_features", num_features)
print("num_movies",   num_movies)
print("num_users",    num_users)

#  From the matrix, we can compute statistics like average rating.
tsmean =  np.mean(Y[0, R[0, :].astype(bool)])
print(f"Average rating for movie 1 : {tsmean:0.3f} / 5" )

def cofi_cost_func_for_loop(X, W, b, Y, R, lambda_):
    """
    Returns the cost for the content-based filtering
    Args:
      X (ndarray (num_movies,num_features)): matrix of item features
      W (ndarray (num_users,num_features)) : matrix of user parameters
      b (ndarray (1, num_users)            : vector of user parameters
      Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
      R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
      lambda_ (float): regularization parameter
    Returns:
      J (float) : Cost
    """
    nm, nu = Y.shape
    J = 0

    ### START CODE HERE ###  
    # Compute the cost function and gradient for collaborative filtering.
    # Concretely, you should first implement the cost function (without regularization).    
    # After that, you should implement the gradient.
    # Note: X_grad should be a matrix of the same size as X
    
    # j -> number of users 
    for j in range(nu):
        # i -> number of movies
        for i in range(nm):
            cofi_cost_func = (np.dot(W[j,:], X[i,:].T) + b[0,j] - Y[i,j])**2
            J += cofi_cost_func * R[i,j]

   
    J = J/2

    # Regularization
    J += (lambda_/2) * np.sum(W**2) + (lambda_/2) * np.sum(X**2)


    return J
    ### END CODE HERE ###


# LINEAR ALEGEBRA VERSION --> MUCH FASTER!!!
# 1. Vectorized version of the cost function
# will learn about this later in the course
def cofi_cost_func_v(X, W, b, Y, R, lambda_):
    """
    Returns the cost for the content-based filtering
    Vectorized for speed. Uses tensorflow operations to be compatible with custom training loop.
    Args:
      X (ndarray (num_movies,num_features)): matrix of item features
      W (ndarray (num_users,num_features)) : matrix of user parameters
      b (ndarray (1, num_users)            : vector of user parameters
      Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
      R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
      lambda_ (float): regularization parameter
    Returns:
      J (float) : Cost
    """
    j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R
    J = 0.5 * tf.reduce_sum(j**2) + (lambda_/2) * (tf.reduce_sum(X**2) + tf.reduce_sum(W**2))
    return J

# Test-1 
# Reduce the data set size so that this runs faster
num_users_r = 4
num_movies_r = 5 
num_features_r = 3

X_r = X[:num_movies_r, :num_features_r]
W_r = W[:num_users_r,  :num_features_r]
b_r = b[0, :num_users_r].reshape(1,-1)
Y_r = Y[:num_movies_r, :num_users_r]
R_r = R[:num_movies_r, :num_users_r]

print("Y_r", Y_r.shape, "R_r", R_r.shape)
print("X_r", X_r.shape, "W_r", W_r.shape)

# Evaluate cost function
J = cofi_cost_func_v(X_r, W_r, b_r, Y_r, R_r, 1.5);
print(f"Cost: {0 if J is None else J:0.2f}")
# Expected answer - 13.67 without regularisation and 28.09 with regularisation
