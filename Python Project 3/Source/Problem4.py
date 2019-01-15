#This was taken and referred from Lecture 6 Source Code: 

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split

irisdataset=datasets.load_iris()
x=irisdataset.data
y=irisdataset.target

model= KNeighborsClassifier(n_neighbors=1)
model.fit(x,y)
print(x)
print(model.predict([[1,2,3,4],[2,3,4,5]]))

print(model.score(x,y))

#print(x)
#print(y)
#print(model)
