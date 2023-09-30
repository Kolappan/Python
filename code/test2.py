import numpy as np

def my_dense(a_in, W, b):
    """
    Computes dense layer
    Args:
      a_in (ndarray (n, )) : Data, 1 example 
      W    (ndarray (n,j)) : Weight matrix, n features per unit, j units
      b    (ndarray (j, )) : bias vector, j units  
    Returns
      a_out (ndarray (j,))  : j units|
    """
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):               
        w = W[:,j]                                    
        z = np.dot(w, a_in) + b[j]         
        a_out[j] = g(z)               
    return(a_out)

# 3 features
a_in = np.array([[1, 2], [3, 4]])
print(f"a_in.shape = {a_in.shape}")
# 3 features, 4 units 
W = np.array([[1, 2,4, 5], [7, 8 ,10,11]]) 
print(f"W.shape = {W.shape}")
b = np.array([1, 2, 3, 4])
print(f"b.shape = {b.shape}")
a_out = my_dense(a_in, W, b)
print(f"a_out.shape = {a_out.shape}")
print(f"a_out = {a_out}")