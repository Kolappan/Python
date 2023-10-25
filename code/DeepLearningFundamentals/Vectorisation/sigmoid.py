import math
import public_tests
import numpy as np

# GRADED FUNCTION: basic_sigmoid

def sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    
    s =  1/ (1+ np.exp(-x))
    # YOUR CODE ENDS HERE
    
    return s

print("np_sigmoid(1) = " + str(sigmoid(1)))
