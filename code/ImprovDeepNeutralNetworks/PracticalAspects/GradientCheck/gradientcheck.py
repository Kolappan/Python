import numpy as np 

def forward_propagation(x, theta):
    """
    Implement the linear forward propagation (compute J) presented in Figure 1 (J(theta) = theta * x)
    
    Arguments:
    x -- a real-valued input
    theta -- our parameter, a real number as well
    
    Returns:
    J -- the value of function J, computed using the formula J(theta) = theta * x
    """
    
    # (approx. 1 line)
    # J = 
    # YOUR CODE STARTS HERE
    
    J =  theta * x 
    
    # YOUR CODE ENDS HERE
    
    return J

x, theta = 2, 4
J = forward_propagation(x, theta)
print ("J = " + str(J))

def backward_propagation(x, theta):
    """
    Computes the derivative of J with respect to theta (see Figure 1).
    
    Arguments:
    x -- a real-valued input
    theta -- our parameter, a real number as well
    
    Returns:
    dtheta -- the gradient of the cost with respect to theta
    """
    
    # (approx. 1 line)
    # dtheta = 
    # YOUR CODE STARTS HERE
    
    dtheta = x 
    
    # YOUR CODE ENDS HERE
    
    return dtheta

x, theta = 3, 4
dtheta = backward_propagation(x, theta)
print ("dtheta = " + str(dtheta))


def gradient_check(x, theta, epsilon=1e-7, print_msg=False):
    """
    Implement the gradient checking presented in Figure 1.
    
    Arguments:
    x -- a float input
    theta -- our parameter, a float as well
    epsilon -- tiny shift to the input to compute approximated gradient with formula(1)
    
    Returns:
    difference -- difference (2) between the approximated gradient and the backward propagation gradient. Float output
    """
    
    # Compute gradapprox using right side of formula (1). epsilon is small enough, you don't need to worry about the limit.
    # (approx. 5 lines)
    # theta_plus =                                 # Step 1
    # theta_minus =                                # Step 2
    # J_plus =                                    # Step 3
    # J_minus =                                   # Step 4
    # gradapprox =                                # Step 5
    # YOUR CODE STARTS HERE
    theta_plus = theta + epsilon
    theta_minus = theta - epsilon
    J_plus = forward_propagation(x, theta_plus)
    J_minus = forward_propagation(x, theta_minus)
    gradapprox = (J_plus - J_minus) / (2 * epsilon)
    print("gradapprox", gradapprox)
    
    
    # YOUR CODE ENDS HERE
    
    # Check if gradapprox is close enough to the output of backward_propagation()
    #(approx. 1 line) DO NOT USE "grad = gradapprox"
    # grad =
    # YOUR CODE STARTS HERE
    
    grad = backward_propagation(x, theta)
    print("grad", grad)
    
    # YOUR CODE ENDS HERE
    
    #(approx. 3 lines)
    # numerator =                                 # Step 1'
    # denominator =                               # Step 2'
    # difference =                                # Step 3'
    # YOUR CODE STARTS HERE
    numerator = np.linalg.norm (grad - gradapprox)
    denominator = np.linalg.norm (grad) +  np.linalg.norm(gradapprox)
    difference =  numerator / denominator
    
    # YOUR CODE ENDS HERE
    if print_msg:
        if difference > 2e-7:
            print ("\033[93m" + "There is a mistake in the backward propagation! difference = " + str(difference) + "\033[0m")
        else:
            print ("\033[92m" + "Your backward propagation works perfectly fine! difference = " + str(difference) + "\033[0m")
    
    return difference

x, theta = 3, 4
difference = gradient_check(x, theta, print_msg=True)