# Library Creation:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title} \n Author: {self.author} \n Available: {'Yes' if self.is_available else 'No'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            print('Books available in the library')
            for book in self.books:
                print(book)
        else:
            print('No books available in library')

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You Borrowed {book.title} in the library")
                else:
                    print(f"sorry! {book.title} is not available in the library")
                    return
        print('Book not found in the library')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"Thank you for returning {book.title}.")
                return
        print('book is not found in library')

    def display_options(self):
        print('\nOptions: ')
        print('1. Display all books')
        print('2. Borrow a Book')
        print('3. Return a Book')
        print('4. Exit')


library = Library()
book1 = Book('Python Programming', 'Selva')
book2 = Book('Master in Java', 'Hari')
book3 = Book('SQL', 'Niru')
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

while True:
    library.display_options()
    choice = input('Enter a Option: ')
    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input('Enter a book title: ')
        library.lend_book(title)
    elif choice == '3':
        title = input('Enter a book title: ')
        library.return_book(title)
    elif choice == '4':
        print('Existing the library. Thank you!')
        exit()
    else:
        print('invalid Input, please choose the correct option')
