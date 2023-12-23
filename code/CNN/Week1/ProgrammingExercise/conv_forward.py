import numpy as np
import padding as pd
import conv_single_step as cs

def conv_forward(A_prev, W, b, hparameters):
    """
    Implements the forward propagation for a convolution function
    
    Arguments:
    A_prev -- output activations of the previous layer, 
        numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    W -- Weights, numpy array of shape (f, f, n_C_prev, n_C)
    b -- Biases, numpy array of shape (1, 1, 1, n_C)
    hparameters -- python dictionary containing "stride" and "pad"
        
    Returns:
    Z -- conv output, numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache of values needed for the conv_backward() function
    """
    
    # Retrieve dimensions from A_prev's shape (≈1 line)  
    # (m, n_H_prev, n_W_prev, n_C_prev) = None
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

    # Retrieve dimensions from W's shape (≈1 line)
    # (f, f, n_C_prev, n_C) = None
    (f, f, n_C_prev, n_C) = W.shape
    
    # Retrieve information from "hparameters" (≈2 lines)
    # stride = None
    # pad = None
    stride = hparameters["stride"]
    pad = hparameters["pad"]

    # Compute the dimensions of the CONV output volume using the formula given above. 
    # Hint: use int() to apply the 'floor' operation. (≈2 lines)
    # n_H = None
    # n_W = None
    n_H = int((n_H_prev - f + 2 * pad) / stride) + 1
    n_W = int((n_W_prev - f + 2 * pad) / stride) + 1

    # Initialize the output volume Z with zeros. (≈1 line)
    # Z = None
    Z = np.zeros((m, n_H, n_W, n_C))

    # Create A_prev_pad by padding A_prev
    # A_prev_pad = None
    A_prev_pad = pd.zero_pad(A_prev, pad)

    # for i in range(None):               # loop over the batch of training examples
        # a_prev_pad = None               # Select ith training example's padded activation
    for i in range(m):
        a_prev_pad = A_prev_pad[i,:,:,:]
        # for h in range(None):           # loop over vertical axis of the output volume
        # Find the vertical start and end of the current "slice" (≈2 lines)
        for h in range(n_H):
            vert_start = h * stride
            vert_end = vert_start + f
            for w in range(n_W):
            # for w in range(None):       # loop over horizontal axis of the output volume
            # Find the horizontal start and end of the current "slice" (≈2 lines)
                horiz_start = w * stride
                horiz_end = horiz_start + f
                # for c in range(None):   # loop over channels (= #filters) of the output volume
                # Use the corners to define the (3D) slice of a_prev_pad (See Hint above the cell). (≈1 line)
                # a_slice_prev = None
                for c in range(n_C):
                # YOUR CODE STARTS HERE
                    a_slice_prev = a_prev_pad[vert_start:vert_end,horiz_start:horiz_end,:]
                # YOUR CODE ENDS HERE

                # Convolve the (3D) slice with the correct filter W and bias b, to get back one output neuron. (≈3 line)
                # weights = None
                # biases = None
                # Z[i, h, w, c] = None
                # YOUR CODE STARTS HERE
                    weights = W[:,:,:,c]
                    biases = b[:,:,:,c]
                    Z[i, h, w, c] = cs.conv_single_step(a_slice_prev, weights, biases)
                # YOUR CODE ENDS HERE

        # Save information in "cache" for the backprop
    cache = (A_prev, W, b, hparameters)

    return Z, cache


