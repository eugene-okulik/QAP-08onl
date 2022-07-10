# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать книгу,
# возвращать, бронировать. Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    reserved = False
    taken = False

    def __init__(self, author, name, pages, isbn):
        self.author = author
        self.name = name
        self.pages = pages
        self.isbn = isbn

    def set_reserve(self, reserved):
        self.reserved = reserved

    def set_taken(self, taken):
        self.taken = taken


class User:

    @staticmethod
    def reserve(book):
        book.set_reserve(True)
        print("You have reserved the book")

    @staticmethod
    def take(book):
        if book.taken or book.reserved is True:
            print("You can't take this book")
        else:
            print("You can take this book")
            book.set_taken(True)

    @staticmethod
    def return_book(book):
        book.set_taken(False)
        print('Thank you for returning')


book_1 = Book("Daniel Keyes", "Flowers for Algernon", 300, "12347")
book_2 = Book("Daniel Keyes", "The Minds of Billy Milligan", 420, "56783")
book_3 = Book("Daniel Keyes", "The Milligan Wars", 512, "7839")

user_1 = User()
user_2 = User()
user_3 = User()

user_1.take(book_1)
user_2.return_book(book_2)
user_3.take(book_3)
user_2.reserve(book_2)
