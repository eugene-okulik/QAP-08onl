# Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
# зарезервирована ли книга или нет.
# Создайте класс пользователь который может брать книгу, возвращать,
# бронировать. Если другой пользователь хочет взять зарезервированную
# книгу (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self._pages = pages
        self._isbn = isbn
        self.reserve_status = True
        self.user = None

    @property
    def pages(self):
        return self._pages

    @property
    def isbn(self):
        return self._isbn


class Libr:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def get_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return False


class User:
    def __init__(self):
        pass

    def get_book(self, name, author, libr):
        book = libr.get_book(name)
        if book:
            if book.reserve_status:
                book.reserve_status = False
                book.user = self
                print(f'I take the book {name} {author}')
            else:
                print(f'Book {name} {author} reserved, choose another')

    def return_book(self, name, author, libr):
        book = libr.get_book(name)
        if book.user == self:
            book.user = None
            book.reserve_status = True
            print(f'I returned book {name} {author}')


book1 = Book("'Метод'", "123456789", 100, "Даниил Лектор")
book2 = Book("'Краткие ответы на большие вопросы'", "987654321", 200, "Стивен Хокинг")
book3 = Book("'Природа пространства и времени'", "123984567", 300, "Стивен Хокинг")

lib = Libr()
lib.add_books(book1)
lib.add_books(book2)
lib.add_books(book3)

user1 = User()
user2 = User()

user1.get_book("'Метод'", "Даниил Лектор",  lib)
user2.get_book("'Краткие ответы на большие вопросы'", "Стивен Хокинг", lib)
user1.get_book("'Природа пространства и времени'", "Стивен Хокинг", lib)
user2.return_book("'Краткие ответы на большие вопросы'", "Стивен Хокинг", lib)
