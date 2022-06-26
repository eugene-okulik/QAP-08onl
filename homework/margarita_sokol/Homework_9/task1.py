# Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
# зарезервирована ли книга или нет.
# Создайте класс пользователь который может брать книгу, возвращать,
# бронировать. Если другой пользователь хочет взять зарезервированную
# книгу (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.user = None

    def set_user(self, user):
        self.user = user

    def set_reserved(self, value):
        self.reserved = value


class User:
    def take(self, book):
        if book.user is not None or book.reserved is True:
            print(f'{book.name} book is currently unavailable')
        else:
            print(f'Please, take a book {book.name}')
            book.set_user(self)

    @staticmethod
    def replace(book):
        book.set_user(None)

    @staticmethod
    def reserve(book):
        book.set_reserved(True)


book1 = Book('Harry Potter', 'J. K. Rowling', 528, '217021')
book2 = Book('The Green Mile', 'Stephen King', 380, '708534')
book3 = Book('Gone With the Wind', 'Margaret Mitchel', 624, '978512')
userA = User()
userB = User()
userC = User()

userA.take(book3)
userB.reserve(book1)
userC.take(book1)
