#Part 4
#Sample lists for python and webapplications
webApplications = ['Tony', 'Frank','Paul','Eddie','Brady','Blake']
python = ['Clark','Tony','Eddie','Harris']

#arraylists for same and different
same = []
different = []

#isClear parameter
isClear = True

#Cycle the WebApplications list
for c in webApplications:
    for x in python:
        if(c==x):
            isClear=False
    if(isClear==False):
        same.append(c)
    else:
        different.append(c)
    isClear = True

#Cycle the Python list
for x in python:
    for c in webApplications:
        if(c==x):
            isClear=False
    if(isClear==True):
        different.append(x)
    isClear = True

#Print Lists
print('Same: ')
for m in same:
    print(m)
print(' ')
print('Different: ')
for n in different:
    print(n)