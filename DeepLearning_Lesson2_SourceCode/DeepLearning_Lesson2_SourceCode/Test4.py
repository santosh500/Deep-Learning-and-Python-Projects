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

t = Features_train
np.split(t,10)
y = 0
arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []
arr10 = []
arr11 = []
arr12 = []
for i in range(0,10):
    arr1.append(Features_train[i])
for i in range(0,10):
    arr1.append(Features_train[i])
for i in range(0,10):
    arr1.append(Features_train[i])
print(arr1)


