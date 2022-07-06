# Создайте класс book с именем книги, автором, кол-м страниц,
# ISBN, флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь который может брать книгу, возвращать, бронировать.
# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
    reserved = False
    user = None

    def set_user(self, user):
        self.user = user

    def set_reserved(self, value):
        self.reserved = value


class User:
    def take(self, book):
        if book.user is not None or book.reserved is True:
            print(f'{book.name} you can not take')
        else:
            print(f'{book.name} you can take')
            book.set_user(self)

    @staticmethod
    def replace(book):
        book.set_user(None)

    @staticmethod
    def reserve(book):
        book.set_reserved(True)


book1 = Book('Book1', 'Author1', 123, '12345')
book2 = Book('Book2', 'Author2', 234, '23456')
book3 = Book('Book3', 'Author3', 345, '34567')

user1 = User()
user2 = User()
user3 = User()

user1.take(book3)
user2.reserve(book1)
user3.take(book1)
user1.replace(book2)
