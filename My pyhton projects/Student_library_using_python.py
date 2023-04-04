class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        
    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for books in self.books:
            print(" * " + books)
    
    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days ")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this books is already been issued to someone else or either not availabe .Please wait until the book is available")    
            return False
        
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoy reading it.HAve a great day ahead!")                 

class Student:
    
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returntBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == '__main__':
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''====Welcome to central Library===
        Please choose an option :
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit a Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a Choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBooks(student.requestBook())    
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()        
        else:
            print("Invalid choice")    
        
        
    

