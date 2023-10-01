import numpy as np
import matplotlib.pyplot as plt
from utils import *


# Load the dataset
X_train, X_val, y_val = load_data()

# Display the first five elements of X_train
print("The first 5 elements of X_train are:\n", X_train[:5])  

# Display the first five elements of X_val
print("The first 5 elements of X_val are\n", X_val[:5])  

# Display the first five elements of y_val
print("The first 5 elements of y_val are\n", y_val[:5])  

print ('The shape of X_train is:', X_train.shape)
print ('The shape of X_val is:', X_val.shape)
print ('The shape of y_val is: ', y_val.shape)

# Create a scatter plot of the data. To change the markers to blue "x",
# we used the 'marker' and 'c' parameters
plt.scatter(X_train[:, 0], X_train[:, 1], marker='x', c='b') 

# Set the title
plt.title("The first dataset")
# Set the y-axis label
plt.ylabel('Throughput (mb/s)')
# Set the x-axis label
plt.xlabel('Latency (ms)')
# Set axis range
plt.axis([0, 30, 0, 30])
plt.show()

# UNQ_C1
# GRADED FUNCTION: estimate_gaussian

def estimate_gaussian(X): 
    """
    Calculates mean and variance of all features 
    in the dataset
    
    Args:
        X (ndarray): (m, n) Data matrix
    
    Returns:
        mu (ndarray): (n,) Mean of all features
        var (ndarray): (n,) Variance of all features
    """

    m, n = X.shape
    
    ### START CODE HERE ### 
    mu = np.mean(X, axis=0)
    var = np.var(X, axis=0)
    ### END CODE HERE ### 
    
    return mu, var
        
# Estimate mu and sigma2

mu, var = estimate_gaussian(X_train)

print("Mean of each feature:", mu)
print("Variance of each feature:",  var)
    
def select_threshold(y_val, p_val): 
    """
    Finds the best threshold to use for selecting outliers 
    based on the results from a validation set (p_val) 
    and the ground truth (y_val)
    
    Args:
        y_val (ndarray): Ground truth on validation set
        p_val (ndarray): Results on validation set
        
    Returns:
        epsilon (float): Threshold chosen 
        F1 (float):      F1 score by choosing epsilon as threshold
    """ 

    best_epsilon = 0
    best_F1 = 0
    F1 = 0
    
    step_size = (max(p_val) - min(p_val)) / 1000

    ### START CODE HERE ###
    for epsilon in np.arange(min(p_val), max(p_val), step_size):
        predictions = (p_val < epsilon)[:, np.newaxis]
        tp = np.sum(predictions[y_val == 1] == 1)
        fp = np.sum(predictions[y_val == 0] == 1)
        fn = np.sum(predictions[y_val == 1] == 0)
        prec = tp / (tp + fp)
        rec = tp / (tp + fn)
        F1 = (2 * prec * rec) / (prec + rec)
        if F1 > best_F1:
            best_F1 = F1
            best_epsilon = epsilon