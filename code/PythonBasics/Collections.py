import string
import numpy as np

# List

xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"x

print("-------------------------------------")
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"

print("-------------------------------------")

# List Comprehension
print("List Comprehension")
nums = [0, 1, 2, 9, 10]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]
print("list value", nums[3])

# List Comprehension with conditions
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"

print("-------------------------------------")

# Dictionaries

d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
print(d)
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"

# Dictonary Comprehension

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"

animals =  d['cat']
print(animals)  # Prints "cute"

# Sets
# A set is an unordered collection of distinct elements.

animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"

# Tuples
# A tuple is an (immutable) ordered list of values. 
# A tuple is in many ways similar to a list; 
# one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
print(d)
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"


e = {(x): (x, x+1) for x in range(10)}  # Create a dictionary with tuple keys
print(e)
t = (5)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(e[t])       # Prints "5, 6"
print(e[(1)])  # Prints "1, 2"

# Create a dictionary of arrays (lists)
sample_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "potato", "cucumber"],
    "numbers": [1, 2, 3, 4, 5]
}


fruits, vegetables, numbers = sample_dict['fruits'], sample_dict['vegetables'], sample_dict['numbers']

for gradient in [fruits, vegetables, numbers]:
    
    print("gradient", gradient)
        
    ### END CODE HERE ###
    


# Create a list of all alphabets - 2D Array


# Create a list of all alphabets
alphabets = list(string.ascii_lowercase)

# Creating a 2D array with each alphabet in its own row
alphabet_2d_array = [[letter] for letter in alphabets]

print("2D Array", alphabet_2d_array)

# Matrix multipliecation

matrix1 = np.array([[1,1],[2,2],[3,3]]) # (3,2)
matrix2 = np.array([[0],[0],[0]]) # (3,1) 
vector1D = np.array([1,1]) # (2,) 
print("vector1D (2,) shape \n", vector1D.size, "\n")
vector2D = np.array([[1],[1]]) # (2,1)

print("matrix1 (3,2) \n", matrix1,"\n")
print("matrix2 (3,1)\n", matrix2,"\n")
print("vector1D (2,)\n", vector1D,"\n")
print("vector2D (2,1)\n", vector2D)

print("Multiply 2D  matrix and 1D vectors: result is a 2D array\n", 
      np.dot(matrix1,vector1D))

print("Multiply 2D and 1D arrays: result is a 1D array\n", 
      np.dot(matrix1,vector1D))
print("Multiply 2D and 2D arrays: result is a 2D array\n", 
      np.dot(matrix1,vector2D))
print("Adding (3 x 1) vector to a (3 x 1) vector is a (3 x 1) vector\n",
      "This is what we want here!\n", 
      np.dot(matrix1,vector2D) + matrix2)
print("Adding a (3,) vector to a (3 x 1) vector\n",
      "broadcasts the 1D array across the second dimension\n",
      "Not what we want here!\n",
      np.dot(matrix1,vector1D) + matrix2
     )

np.random.seed(0)
probs = np.array([0.3, 0.2, 0.4, 0.1])
print("probs", probs)
print("probs length", len(probs))
print("range", range(len(probs)))

idx = np.random.choice([5,6,7,8], p = probs)
print("idx", idx)