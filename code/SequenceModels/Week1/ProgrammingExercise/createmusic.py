import tensorflow as tf
import keras.layers as tfl
import IPython
import sys
import matplotlib.pyplot as plt
import numpy as np



# You can now use the individual layer classes directly
from keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector
from keras.models import Model
from keras.optimizers import Adam
from keras.utils import to_categorical

# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: djmodel

def djmodel(Tx, LSTM_cell, densor, reshaper):
    """
    Implement the djmodel composed of Tx LSTM cells where each cell is responsible
    for learning the following note based on the previous note and context.
    Each cell has the following schema: 
            [X_{t}, a_{t-1}, c0_{t-1}] -> RESHAPE() -> LSTM() -> DENSE()
    Arguments:
        Tx -- length of the sequences in the corpus
        LSTM_cell -- LSTM layer instance
        densor -- Dense layer instance
        reshaper -- Reshape layer instance
    
    Returns:
        model -- a keras instance model with inputs [X, a0, c0]
    """
    n_values = 90 # number of music values
    image = tf.reshape(image, [-1,])
    reshaper = Reshape((1, n_values))                  # Used in Step 2.B of djmodel(), below
    LSTM_cell = LSTM(n_a, return_state = True)         # Used in Step 2.C
    densor = Dense(n_values, activation='softmax')


    # Get the shape of input values
    n_values = densor.units
    
    # Get the number of the hidden state vector
    n_a = LSTM_cell.units

    # Define the input layer and specify the shape
    X = Input(shape=(Tx, n_values))    

    # Define the initial hidden state a0 and initial cell state c0
    a0 = Input(shape=(n_a,), name='a0')
    c0 = Input(shape=(n_a,), name='c0')
    a = a0
    c = c0

    ### START CODE HERE ###
    # Step 1: Create an empty list of outputs
    outputs = []

    # Step 2: Loop over Tx and generate a value at every time step
    for t in range(Tx):
        # Step 2.A: select the "t"th time step vector from X. 
        x = X[:,t,:]
        # Step 2.B: Use reshaper to reshape x to be (1, n_values) (≈1 line)
        x = reshaper(x)
        # Step 2.C: Perform one step of the LSTM_cell
        a, _, c = LSTM

