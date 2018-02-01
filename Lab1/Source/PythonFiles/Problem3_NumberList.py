#3)
#Sample input
input = [1,3,6,2,-1,2,8,-2,9]
int1=0
int2=1
int3=2
first=input[0]
second=input[1]
third=input[2]
#Store in collection
collection = []
for d in input:
    for y in input:
        for o in input:
            if(not((d==y) or (d==o) or (o==y))):
                tuple = (d,y,o)
                collection.append(tuple)


#Print Triplets
print('Triplets are:')
for u in collection:
    l = u[0]+u[1]+u[2]
    if l==0:
        print (u)


