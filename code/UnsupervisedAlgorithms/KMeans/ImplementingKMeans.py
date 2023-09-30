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

  
    # Useful variables
    m, n = X.shape
    print ("m", m)
    print ("n", n)

    # Set K
    K = centriods.shape[0]

    # You need to return the following variables correctly
    idx = np.zeros(m,dtype=int)
    mindistance = 0

    ### START CODE HERE ###
    for i in range(m):
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

# Select an initial set of centroids (3 Centroids)
initial_centroids = np.array([[3,3], [6,2], [8,5]])

# Find closest centroids using initial_centroids
idx = find_closest_centroids(X, initial_centroids)

# Print closest centroids for the first three elements
print("First three elements in idx are:", idx[:3])


# Compute means based on the closest centroids found in the previous part

def compute_centroids(X, idx, K):
    """
    Returns the new centroids by computing the means of the 
    data points assigned to each centroid.

    Args:
        X (ndarray):   (m, n) Data points
        idx (ndarray): (m,) Array containing index of closest centroid for each 
                        example in X. Concretely, idx[i] contains the index of 
                        the centroid closest to example i
        K (int):       number of centroids

    Returns:
        centroids (ndarray): (K, n) New centroids computed
    """
    ### START CODE HERE ###
    # Useful variables
    m, n = X.shape
    centroids = np.zeros((K, n))

    for k in range(K):
        # get a list of all data points in X assigned to centroid k
        points = X[idx == k]
        centroids[k] = np.mean(points, axis=0)
    return centroids

# valiadation
K = 3
centroids = compute_centroids(X, idx, K)
print("The centroids are:", centroids)

#Run K Means - by showing the plot - this program is given by the tutor
def run_kMeans(X, initial_centroids, max_iters=10, plot_progress=False):
    """
    Runs the K-Means algorithm on data matrix X, where each row of X
    is a single example
    """
    
    # Initialize values
    m, n = X.shape
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    previous_centroids = centroids    
    idx = np.zeros(m)
    plt.figure(figsize=(8, 6))

    # Run K-Means
    for i in range(max_iters):
        
        #Output progress
        print("K-Means iteration %d/%d" % (i, max_iters-1))
        
        # For each example in X, assign it to the closest centroid
        idx = find_closest_centroids(X, centroids)
        
        # Optionally plot progress
        if plot_progress:
            plot_progress_kMeans(X, centroids, previous_centroids, idx, K, i)
            previous_centroids = centroids
            
        # Given the memberships, compute new centroids
        centroids = compute_centroids(X, idx, K)
    plt.show() 
    return centroids, idx

# Load an example dataset
X = load_data()

# Set initial centroids
initial_centroids = np.array([[3,3],[6,2],[6,6]])

# Number of iterations
max_iters = 50

# Run K-Means
centroids, idx = run_kMeans(X, initial_centroids, max_iters, plot_progress=True)