import csv

file1 = open('oneRating.txt','w')
file2 = open('twoRating.txt','w')
file3 = open('threeRating.txt','w')
file4 = open('fourRating.txt','w')
file5 = open('fiveRating.txt','w')

with open('train.csv') as f:
    for line in f:
        if line[0]=='2':
            l = line[2:]
            print(l, end='')
            file2.write(l)
        elif line[0]=='1':
            l = line[2:]
            print(l, end='')
            file1.write(l)
        elif line[0]=='3':
            l = line[2:]
            print(l, end='')
            file3.write(l)
        elif line[0]=='4':
            l = line[2:]
            print(l, end='')
            file4.write(l)
        elif line[0]=='5':
            l = line[2:]
            print(l, end='')
            file5.write(l)




file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
