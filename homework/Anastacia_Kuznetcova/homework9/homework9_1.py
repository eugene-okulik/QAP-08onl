"""Внизу решение задания"""


class Book:
    """Создан класс книг"""
    reserved = False
    user = None

    def __init__(self, name, isbn, pages, author):
        self.name = name
        self.isbn = isbn
        self.pages = pages
        self.author = author

    def set_reserve(self, value):
        """Метод setter резервирования книги"""
        self.reserved = value

    def set_user(self, user):
        """Метод setter пользователя"""
        self.user = user


class User:
    """Класс пользователя"""
    @staticmethod
    def reserve(book):
        """Метод бронирования книги"""
        book.set_reserve(True)

    def get_book(self, book):
        """Метод получения книги"""

        if book.user is not None or book.reserved is True:
            print("Книгу нельзя взять")
        else:
            print("Get book", book.name)
            book.set_user(self)

    @staticmethod
    def return_book(book):
        """Метод возвращения книги"""
        book.set_user(None)


book1 = Book("Оно", "1245563462", 650, "Стивен Кинг")
book2 = Book("Зеленая миля", "23425245", 560, "Стивен Кинг")
book3 = Book("Мизери", "245245245", 530, "Стивен Кинг")

user1 = User()
user2 = User()

user1.reserve(book1)
user2.get_book(book2)
user1.get_book(book2)
user2.return_book(book2)
user1.get_book(book2)
