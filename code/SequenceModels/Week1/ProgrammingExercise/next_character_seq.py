import numpy as np
import rnn_cell_forward
import  DeepLearningFundamentals.Vectorisation.softmax as softmax

def sample(parameters, char_to_ix, seed):
    """
    Sample a sequence of characters according to a sequence of probability distributions output of the RNN

    Arguments:
    parameters -- Python dictionary containing the parameters Waa, Wax, Wya, by, and b. 
    char_to_ix -- Python dictionary mapping each character to an index.
    seed -- Used for grading purposes. Do not worry about it.

    Returns:
    indices -- A list of length n containing the indices of the sampled characters.
    """
    
    # Retrieve parameters and relevant shapes from "parameters" dictionary
    Waa, Wax, Wya, by, b = parameters['Waa'], parameters['Wax'], parameters['Wya'], parameters['by'], parameters['b']
    vocab_size = by.shape[0]
    n_a = Waa.shape[1]
    
    ### START CODE HERE ###
    # Step 1: Create the a zero vector x that can be used as the one-hot vector 
    # Representing the first character (initializing the sequence generation). (≈1 line)
    x = np.zeros(vocab_size,1)
    # Step 1': Initialize a_prev as zeros (≈1 line)
    a_prev = np.zeros(n_a,1)
    
    # Create an empty list of indices. This is the list which will contain the list of indices of the characters to generate (≈1 line)
    indices = []
    
    # idx is the index of the one-hot vector x that is set to 1
    # All other positions in x are zero.
    # Initialize idx to -1
    idx = -1 
    
    # Loop over time-steps t. At each time-step:
    # Sample a character from a probability distribution 
    # And append its index (`idx`) to the list "indices". 
    # You'll stop if you reach 50 characters 
    # (which should be very unlikely with a well-trained model).
    # Setting the maximum number of characters helps with debugging and prevents infinite loops. 
    counter = 0
    newline_character = char_to_ix['\n']

    while (idx != newline_character and counter != 50):
            
            # Step 2: Forward propagate x using the equations (1), (2) and (3)
            # a_next, _ = None
            # YOUR CODE STARTS HERE
            a = np.tanh(np.dot(Wax, x )+ np.dot(Waa,a_prev ) + b)
            z = np.dot(Wya,a) + by
            y = softmax(z)
            # YOUR CODE ENDS HERE
            
            # Step 3: Sample the index of a character within the vocabulary from the probability distribution a_next
            # idx = None
            # YOUR CODE STARTS HERE
            idx = np.random.choice(range(vocab_size), p=y.ravel())
            # YOUR CODE ENDS HERE
            
            # Append the index to "indices"
            indices.append(idx)
            
            # Step 4: Overwrite the input x with one that corresponds to the sampled index `idx`.
            # (see additional hints above)
            # x = None
            # YOUR CODE STARTS HERE
            x = np.zeros((vocab_size,1))    # create a vector with shape (vocab_size, 1)
            x[idx] = 1                      # set the correct element to 1