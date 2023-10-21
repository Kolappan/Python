""" Import Packages
numpy is a package for scientific computing in python.
deque will be our data structure for our memory buffer.
namedtuple will be used to store the experience tuples.
The gym toolkit is a collection of environments that can be used to test reinforcement learning algorithms. We should note that in this notebook we are using gym version 0.24.0.
PIL.Image and pyvirtualdisplay are needed to render the Lunar Lander environment.
We will use several modules from the tensorflow.keras framework for building deep learning models.
utils is a module that contains helper functions for this assignment. You do not need to modify the code in this file."""
import time
from collections import deque, namedtuple

import gym
import numpy as np
import PIL.Image
import tensorflow as tf
import utils

from pyvirtualdisplay import Display
import tensorflow as tf
from tensorflow import keras
from keras import Sequential

# Set up a virtual display to render the Lunar Lander environment.
Display(visible=0, size=(840, 480)).start();

# Set the random seed for TensorFlow
tf.random.set_seed(utils.SEED)

MEMORY_SIZE = 100_000     # size of memory buffer
GAMMA = 0.995             # discount factor
ALPHA = 1e-3              # learning rate  
NUM_STEPS_FOR_UPDATE = 4  # perform a learning update every C time steps


env = gym.make('LunarLander-v2')
env.reset()
PIL.Image.fromarray(env.render(mode='rgb_array'))

state_size = env.observation_space.shape
num_actions = env.action_space.n

print('State Shape:', state_size)
print('Number of actions:', num_actions)
