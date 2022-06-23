# Библиотека
# Создайте класс book с именем книги, автором, кол-м страниц,
# ISBN, флагом, зарезервирована ли книги или нет.

# Создайте класс пользователь который может брать книгу, возвращать, бронировать.

# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self._pages = pages
        self._isbn = isbn
        self.available = True
        self.current_user = None

    @property
    def pages(self):
        return self._pages

    @property
    def isbn(self):
        return self._isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_by_name(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return False

class User:
    def __init__(self):
        pass

    def get_book(self, name, library):
        book = library.get_book_by_name(name)
        if book:
            if book.available:
                book.available = False
                book.current_user = self
                print(f"I got the book - {name}")
                return True
            else:
                print(f"The book - {name} - is not available")
                return False
        else:
            print("Error")
            return False

    def return_book(self, name, library):
        book = library.get_book_by_name(name)
        if book.current_user == self:
            book.current_user = None
            book.available = True
            print(f"I returned book - {name}")

Book1 = Book("Cats", "AB", 10, "ISBN")
Book2 = Book("Dogs", "CD", 15, "ISBN")

lib = Library()
lib.add_book(Book1)
lib.add_book(Book2)

user1 = User()
user2 = User()

user1.get_book("Cats", lib)
user2.get_book("Cats", lib)
user1.return_book("Cats", lib)
