
#Book class for library system
class Book():
    def __init__(self):
        self.name = 'Default Title'
        self.pages = 100
        self.author = 'Default Author'
#Book Novel and inherited classes
class Novel(Book):
    def __init__(self):
        super(Book, self).__init__()
        self.genre = 'Drama'
        self.hero = 'Hero'
        self.villan = 'Villain'
        self.plot = 'The hero wins'

#book nonfiction and inherted class
class NonFiction(Book):
    _type = ''
    def __init__(self):
        super(Book, self).__init__()


    def setType(self,type):
        self._type=type

    def getType(self):
        print(self._type)

#Person class
class Person():
    _name = ''
    def __init__(self):
        self._name = 'Name'

    def setName(self,name):
        self._name=name

    def getName(self):
        return self._name

#inherited from person
class Student(Person):
    _checkedOut = []
    def __init__(self):
        super(Person, self).__init__()

    def checkOut(self, book):
        self._checkedOut.append(book)

    def getCheckOutList(self):
        return self._checkedOut

class Librarian(Person):
    def __init__(self):
        super(Person, self).__init__()

    def addBookToShelf(self,book,shelf):
        shelf.append(book)

    def notifyLimit(self):
        print('Librarian: You have checked out limit of books')

#Main LIbrary System which is used to utilize the book
class LibrarySystem(Librarian,Book):
    _bookShelf = []
    _librarian = Librarian
    def __init__(self,Librarian,Book):
        Librarian.__init__()
        Book.__init__()
        self._librarian = Librarian


    def returnBook(self, book):
        self._librarian.addBookToShelf(book)

    def getLibrary(self):
        return self._bookShelf

    def getLibrarian(self,Librarian):
        return self._librarian

#Create Librarian for Library System
print('New librarian named Alice Cooper is the librarian')
librarian = Librarian()
librarian.setName('Alice Cooper')

#Add books to library (can be either Novel or Nonficiton)
print('Books are added to the library')
newBook = Novel()
newBook.name = 'Hunger Games'
newBook.author = 'Suzanne Collins'
newBook.pages = 350
newBook.hero = 'Catniss Everdeen'
newBook.villain = 'Game Designer'
newBook.plot = 'Story of 13 disctricts and government corruption within them'
librarySystem = LibrarySystem(librarian,newBook)
librarySystem.addBookToShelf(newBook,librarySystem.getLibrary())
newBook = Novel()
newBook.genre
newBook.name='Game of Thrones'
newBook.pages = 655
newBook.author='George R.R Martin'
newBook.hero = 'Tyrion Lannister'
newBook.villain = 'Cersei Lannister'
newBook.plot = 'Game of Thrones is about a battle of 5 kingdoms and trying to get Iron Throne'
librarySystem.addBookToShelf(newBook,librarySystem.getLibrary())
nfBook = NonFiction()
nfBook.name = 'Cracking the Code Interview'
nfBook.author = 'McDowell'
nfBook.pages = 500
nfBook.setType('Academic')
librarySystem.addBookToShelf(nfBook,librarySystem.getLibrary())
nfBook = NonFiction()
nfBook.name = 'The Bible'
nfBook.author = 'Various'
nfBook.pages = 900
nfBook.setType('Religious')
librarySystem.addBookToShelf(nfBook,librarySystem.getLibrary())
print('The books added are: ')
count = 1
for i in librarySystem.getLibrary():
    print(count)
    count += 1
    print('Title: ' +i.name + '\n'+ 'Author: ' + i.author)
#bookShelf.append(newBook)


#Student enters name and then checks out books
studentName = input( librarySystem.getLibrarian(librarian).getName() + ': You are the new student, what is your name: ')
newStudent = Student()
newStudent.setName(studentName)
done = False
while(done==False):
    book = input(librarySystem.getLibrarian(librarian).getName() + ': Hello, ' + newStudent.getName() + ', what book would you like to check out?')
    shelf = librarySystem.getLibrary()
    for i in shelf:
        if(i.name ==book):
            newStudent.checkOut(i)
    val = input(librarySystem.getLibrarian(librarian).getName() + ': Are you done using library- Y or N?')
    if(val=='Y'):
        done=True
checkList = newStudent.getCheckOutList()

#Librarian tells the student what books they checked out
print(librarySystem.getLibrarian(librarian).getName() + ': Thank you for using Library. You checked out:')
for i in checkList:
    print(i.name)




