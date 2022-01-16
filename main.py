class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this Library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Pls keep it safe and return it in 30 days"
            )
            self.books.remove(bookName)
            
        else:
            print("Sorry! the book is not available")
            

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks! For returning the book! Hope you enjoyed reading the book..")


class Student:
    def requestBook(self):
        self.book = input("Enter the book needed by you: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book that you want to return: ")
        return self.book


if __name__ == "__main__":
    mainLibrary = Library(["Algorithm", "Maths", "Pyhton Tutorial", "Django-Python Framework", "Clrs"])
    student = Student()
    print("===========Welcome to central library===========")
    while True:
        welcomeMsg = """
        Pls Chose an option:
        1. Listing all the Books
        2. Request a book
        3. Return a book
        4. Exit the library
        """
        try:
            print(welcomeMsg)
            a = int(input("Enter a Choice: "))

            if a == 1:
                mainLibrary.displayAvailableBooks()
            elif a == 2:
                mainLibrary.borrowBook(student.requestBook())
            elif a == 3:
                mainLibrary.returnBook(student.returnBook())
            elif a == 4:
                break
            else:
                I=print("Invalid Choice!")
        except ValueError:
            print("Pls enter a valid value")
        except Exception as e:
            print(f"there is an error {e}")
