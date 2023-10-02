import numpy as np
from numpy.core.fromnumeric import size


# Create predictions and y_val arrays
predictions = np.array([6, 7, 8, 9])
y_val = np.array(['a','b','c','d'])

# First statement
a = np.sum(predictions[y_val == 'a'] == 6)

# Second statement
b = np.sum((predictions == 7) & (y_val == 'b'))

print ("a", a)  
print ("b", b)