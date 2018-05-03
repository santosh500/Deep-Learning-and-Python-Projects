import time
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
# Step 1: Read in data
# using TF Learn's built in function to load MNIST data to the folder data/mnist
MNIST = input_data.read_data_sets("/data/mnist", one_hot=True)
iris = datasets.load_iris()
iris_features = iris.data
iris_labels = iris.target
print('Iris Target')
print(len(iris.target))
print('Iris Data')
print(len(iris.data))
Features_train, Features_test, Labels_train, Labels_test = train_test_split(iris_features, iris_labels, test_size=0.2, train_size=0.8)
print('Iris Train')
print(Features_train)
print('Iris Test')
print(Features_test)
print(len(Features_train))
print(len(Features_test))

#Training parameters
learning_rate = 0.01
batch_size = 120
n_epochs = 25

#X and Y
X = tf.placeholder(tf.float32, [batch_size, 4])
Y = tf.placeholder(tf.float32, [batch_size, 3])

#w and b
w = tf.Variable(tf.random_normal(shape=[4, 3], stddev=0.01), name="weights")
b = tf.Variable(tf.zeros([1, 3]), name="bias")

#logitslogits = tf.matmul(X, w) + b
logits = tf.matmul(X, w) + b
print(logits)

#loss function
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y)
loss = tf.reduce_mean(entropy) # computes the mean over examples in the batch

#optimizer function
optimizer =tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)
init = tf.global_variables_initializer()

#
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    n_batches = int(len(Features_train)/batch_size)
    t = 0
    k = 0
    for i in range(n_epochs): # train the model n_epochs times
            #X_batch, Y_batch = iris.next_batch(batch_size)
        sess.run([optimizer, loss], feed_dict={X: Features_train, Y:Labels_train})

        print(t)
        t+=1
        print(k)
        k+=1
    writer.close()
# average loss should be around 0.35 after 25 epochs