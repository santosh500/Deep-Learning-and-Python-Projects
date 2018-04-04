import time
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#Data set from MNIST
dataset = input_data.read_data_sets("/data/mnist", one_hot=True)
#Parameters
learningRate = 0.01
hyperParameter = 0.5
horizontalPixels = 28
verticalPixels=28
labelVariations = 10
# Placeholders and Variables
X = tf.placeholder(tf.float32, [50, horizontalPixels*verticalPixels])
Y = tf.placeholder(tf.float32, [50, labelVariations])
weight = tf.Variable(tf.random_normal(shape=[horizontalPixels*verticalPixels, labelVariations], stddev=0.01))
bias = tf.Variable(tf.zeros([1, labelVariations]))
#Logistic Regression and Loss Functions
logisticRegression = tf.matmul(X, weight) + bias
generalLoss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logisticRegression, labels=Y))
regulationLoss = tf.nn.l2_loss(weight)
totalLoss= (hyperParameter * regulationLoss) + generalLoss
# Gradient Descent Optimizer
GDOptimizer =tf.train.GradientDescentOptimizer(learning_rate=learningRate).minimize(totalLoss)
#Run Session
with tf.Session() as session:
    #Find model for optimizer
    session.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/logisticRegressionDLLab', session.graph)
    #Number of epochs (50)
    for i in range(50):
        #Number of batches (50)
        for _ in range(50):
            #Divides into Xset and Yset for each batch
            Xset, Yset = dataset.train.next_batch(50)
            # Divides into Xset and Yset for each batch
            session.run([GDOptimizer, generalLoss], feed_dict={X: Xset, Y: Yset})
    writer.close()

    #Find Accuracy
    accuratePredictions = 0
    for i in range(200):
        Xset, Yset = dataset.test.next_batch(50)
        nullVal, loss_batch, logits_batch = session.run([GDOptimizer, totalLoss, logisticRegression], feed_dict={X: Xset, Y:Yset})
        predictions = tf.nn.softmax(logits_batch)
        totalCorrect = tf.equal(tf.argmax(predictions, 1), tf.argmax(Yset, 1))
        accuracy = tf.reduce_sum(tf.cast(totalCorrect, tf.float32))
        accuratePredictions += session.run(accuracy)
    print( "Correct Predictions Rate {0}".format(accuratePredictions / 10000))
