class Book:

    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn

    reserved = False
    taken = False

    def set_reserved(self, reserved):
        self.reserved = reserved

    def set_taken(self, taken):
        self.taken = taken


class User:

    @staticmethod
    def take(book):
        if book.taken or book.reserved is True:
            print("You can't take this book -", book.name)
        else:
            print("You can take this book -", book.name)
            book.set_taken(True)

    @staticmethod
    def return_book(book):
        book.set_taken(False)
        print('Thank you for returning')

    @staticmethod
    def reserved_book(book):
        book.set_reserved(True)
        print('You reserved this book')


book_1 = Book('Duma Key', '12345', 670, 'Stephen King')
book_2 = Book('Kudjo', '67890', 400, 'Stephen King')
book_3 = Book('Thinner', '102938', 309, 'Stephen King')

user_1 = User()
user_2 = User()
user_3 = User()

user_1.take(book_3)
user_2.reserved_book(book_2)
user_3.take(book_2)
user_3.reserved_book(book_1)
user_1.return_book(book_3)
