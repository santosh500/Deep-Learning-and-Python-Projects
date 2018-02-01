import re

#1)
isOverall=False
while (isOverall==False):
    str1=str(input('Give a Password: '))
    #Determines between 6-16 characters
    lengthWord=int(len(str1))
    isSuccess = True;
    if((lengthWord>5) and (lengthWord<17)):
        isSuccess=False;

    # Determines if contains number
    isNum = True;
    for letter in str1:
        if letter.isdigit():
            isNum = False
            break

    # Determines if special character
    isSpecial=True
    re.findall('[^A-Za-z0-9]',str1)
    if re.findall('[^A-Za-z0-9]',str1):
        isSpecial=False

    # Determines if uppercase letter and lowercase letter
    isCapital=True
    isLower = True
    for letter in str1:
        if(letter.islower()):
            isLower =False
        if letter.isupper():
            isCapital = False


    if(isCapital==False and isLower==False and isSpecial==False and isNum==False and isSuccess==False):
        print('Good Password')
        isOverall=True
    else:
        if(isCapital==True):
            print("Needs uppercase letter")
        if (isLower == True):
            print("Needs lowercase letter")
        if (isSpecial == True):
            print("Needs Special Character")
        if (isSuccess == True):
            print("Needs to be between 6-16 characters")
        if (isNum == True):
            print("Needs number")