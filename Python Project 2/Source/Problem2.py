#Contains the contact list
contact_list=[{"name":"Paul","number":"9134869697","email":"santosh@gmail.com"},
              {"name": "Tony", "number": "8169590423", "email": "king94@gmail.com"},
              {"name": "Kevin", "number": "18004522342", "email": "kingkevin95@yahoo.com"}]

#display contacts
def displayContactsName(name):
    for i in contact_list:
        if((i["name"])==name):
            print(i)

#displayContacts Number
def displayContactsNumber(number):
    for i in contact_list:
        if((i["number"])==number):
            print(i)

#Edit contact by name
def editContactByName(name,parameter,value):
    for i in contact_list:
        if((i["name"])==name):
            if(parameter=='a'):
                i["name"] = value
            elif(parameter=='b'):
                i["number"] = value
            elif (parameter == 'c'):
                i["email"] = value

def displayContactList():
    for i in contact_list:
        print(i)


#main program and menu
isValid = False
while(isValid==False):
    value = input("Click on a value: \n a) Display Contact by Name \n b) Display contact by number \n c) Edit contact by name \n d) Exit")
    if value=='a':
        print('a')
        choiceA = input('a) Give Name')
        displayContactsName(choiceA)
        displayContactList()
        #isValid = True
    elif value=='b':
        print('b')
        choiceB = input('b) Give Number')
        displayContactsNumber(choiceB)
        displayContactList()
        #isValid = True
    elif value=='c':
        print('c')
        choiceCa = input('a) Give a Name')
        choiceCb = input('a) Which feature to edit \n a) Name \n b) Number \n c) Email')
        choiceCc = input('a) What would you like to change it to: ')
        editContactByName(choiceCa,choiceCb,choiceCc)
        displayContactList()
        #isValid = True
    elif value=='d':
        print('d')
        displayContactList()
        isValid = True
    else:
        print('choose either a,b,c')





