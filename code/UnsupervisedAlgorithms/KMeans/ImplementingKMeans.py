import numpy as np
import matplotlib.pyplot as plt
from utils import *


def find_closest_centroids (X, centriods):
    """ Computes Centroid memberships for every example
    Args: 

        X(ndarray): (m,n) Input Values
        centriods (ndarray): (K,n) Centriods

    Returns:
        idx(array_like): (m,) closest centriods
    
    """

    print ("X.shape[0]", X.shape[0])

    # Set K
    K = centriods.shape[0]

    # You need to return the following variables correctly
    idx = np.zeros(X.shape[0],dtype=int)
    mindistance = 0

    ### START CODE HERE ###
    for i in range(X.shape[0]):
        # Array to hold the distance between x[i] and each centroid[j]
        distance=[]
        for j in range(K):
            norm_ij = np.linalg.norm(X[i]-centriods[j])
            distance.append(norm_ij)
        idx[i] = np.argmin(distance)

    return idx


# Load an example dataset that we will be using
X = load_data()

print("First five elements of X are:\n", X[:5]) 
print('The shape of X is:', X.shape)

