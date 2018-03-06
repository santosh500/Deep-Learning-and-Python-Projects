import pandas as pd
import csv

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

print(iris.data)
print(iris.target)
print(iris.target_names)
print(iris.data[0][2])

#import data for IXIC.csv from Excel Spreadsheet
mainData = []
with open('IXIC.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row1 = []
        print(row['Adj Close'], row['Volume'])
        row1.append(float(row['Open']))
        row1.append(float(row['High']))
        row1.append(float(row['Low']))
        row1.append(float(row['Close']))
        row1.append(float(row['Adj Close']))
        row1.append(float(row['Volume']))
        mainData.append(row1)


#Data Edit
names2 = []
vars2 = []
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Average')
names2.append('Average')
names2.append('Bad')
names2.append('Average')
names2.append('Average')
names2.append('Bad')
names2.append('Bad')
names2.append('Bad')
names2.append('Average')
names2.append('Average')
names2.append('Average')
names2.append('Average')
names2.append('Average')
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(1)
vars2.append(1)
vars2.append(2)
vars2.append(1)
vars2.append(1)
vars2.append(2)
vars2.append(2)
vars2.append(2)
vars2.append(1)
vars2.append(1)
vars2.append(1)
vars2.append(1)
vars2.append(1)

print(mainData)
print(names2)



mainData2 = []
names3=[]
vars3=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]


lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(mainData, vars2).transform(mainData)
print(X_r2)
x=[]
y=[]
for i in X_r2:
    print(i[0])
    x.append(i[0])
    y.append(i[1])
print(y)


for i in range(0, len(names2)):
    if names2[i] == 'Good':
        print(x[i])
        red = x[i]
        x2.append(red)
        y2.append(y[i])

good = len(x2)
for i in range(0, len(names2)):
    if names2[i] == 'Average':
        print(x[i])
        red = x[i]
        x3.append(red)
        y3.append(y[i])
        # y2.append[y[names2.index(i)]]
average = len(x2)
for i in range(0, len(names2)):
    if names2[i] == 'Bad':
        print(x[i])
        red = x[i]
        x4.append(red)
        y4.append(y[i])
bad = len(x2)
print(x2)
print(y2)

for i in range(0,len(x2)):
    plt.plot(x2, y2, 'ro')

for i in range(0,len(x3)):
    plt.plot(x3, y3, 'bo')

for i in range(0,len(x4)):
    plt.plot(x4, y4, 'go')

plt.axis([-5, 5, -2, 2])

red1 = mpatches.Patch(color='red', label='Good')
plt.legend(handles=[red1])
blue1 = mpatches.Patch(color='blue', label='Average')
plt.legend(handles=[blue1])
green1 = mpatches.Patch(color='green', label='Bad')


colors = ["g", "b", "r"]
texts = ["Bad", "Average","Good"]
patches = [ plt.plot([],[], marker="o", ms=10, ls="", mec=None, color=colors[i],
            label="{:s}".format(texts[i]) )[0]  for i in range(len(texts)) ]
plt.legend(handles=patches,
           loc='upper right', ncol=2, facecolor="white", numpoints=1 )
plt.title('LDA Example')
plt.show()
