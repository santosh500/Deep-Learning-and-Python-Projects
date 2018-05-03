import time
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# Step 1: Read in data
# using TF Learn's built in function to load MNIST data to the folder data/mnist
MNIST = input_data.read_data_sets("/data/mnist", one_hot=True)
# Step 2: Define parameters for the model
learning_rate = 0.01
batch_size = 128
n_epochs = 25
# Step 3: create placeholders for features and labels
# each image in the MNIST data is of shape 28*28 = 784
# therefore, each image is represented with a 1x784 tensor
# there are 10 classes for each image, corresponding to digits 0 - 9.
# each label is one hot vector.
X = tf.placeholder(tf.float32, [batch_size, 784])
Y = tf.placeholder(tf.float32, [batch_size, 10])
print(MNIST.__sizeof__())
print(MNIST[0])
print(MNIST.train.num_examples)
print(Y)
print(X)