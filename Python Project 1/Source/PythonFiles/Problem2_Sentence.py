#2)
sentence = str(input('Give a sentence of words: '))

words = sentence.split()
#middle words
sentLen = int(len(words))
if(sentLen==2 or sentLen==1):
    print('No middle words')
elif((sentLen%2)==0):
    print('Middle word(s): ',words[int(sentLen/2)-1],',and ',words[int(sentLen/2)])
else:
    print('Middle word(s): ', words[(int(sentLen / 2))])

#Longest Word
length = 0
longWord = ''
for t in words:
    if(len(t)>length):
        length = len(t)
        longWord = t
print('Longest word: ',longWord)

#Reverse sentence in words
words2 = []

print('Reverse words are: ')
for l in words:
    v = l
    y = list(v)
    newWord=''
    count = int(len(y))-1
    for o in range(0,int(len(y))):
        newWord=newWord + y[count]
        count=count-1
    words2.append(newWord)

for w in words2:
    print(w)