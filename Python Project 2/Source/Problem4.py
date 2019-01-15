#import numpy to get the most common number
import numpy as np
a = np.random.rand(15)

b=[]
for i in a:
    b.append(int(round(20*i)))

#Gives input values
print('Input Values: ')
for i in b:
    print(i)

mydict = {}
for i in b:
    if i in mydict:
        val = mydict.get(i,"none")
        mydict[i]=val+1
    else:
        mydict[i]=1

#Show the number count
print('Number Count: ')
print(mydict)


count = 0
longestNum = 0

for i in mydict:
    if(mydict[i]>=count):
        count = mydict[i]
        longestNum = i

#Gives the most common number
print('Most common number',longestNum)
