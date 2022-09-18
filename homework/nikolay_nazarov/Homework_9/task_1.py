# Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
# флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь который может брать книгу, возвращать, бронировать.
# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, book_title, author, pages, isbn):
        self.book_title = book_title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        Library.add_initialized_book(self)

    def some_public_method_1(self):
        pass

    def some_public_method_2(self):
        pass


class Library:
    _books_in_store = []
    _who_took_book_dict = {}
    _books_reserved = []
    _who_reserve_book_dict = {}

    @staticmethod
    def print_who_took_book_dict():
        print("____________________________________")
        print("Какую книгу кто забрал")
        print(Library._who_took_book_dict)
        print("____________________________________")

    @staticmethod
    def print_who_reserve_book_dict():
        print("____________________________________")
        print("Какую книгу кто зарезервировал")
        print(Library._who_reserve_book_dict)
        print("____________________________________")

    @staticmethod
    def remove_book_from_storage(book, user):
        Library._who_took_book_dict[book.book_title] = user.name
        Library._books_in_store.remove(book)

    @staticmethod
    def add_book_to_storage(book):
        Library._who_took_book_dict.pop(book.book_title)
        Library._books_in_store.append(book)

    @staticmethod
    def add_book_to_reserved_list(book, user):
        Library._who_reserve_book_dict[book.book_title] = user.name
        Library._books_reserved.append(book)

    @staticmethod
    def remove_book_from_reserved_list(book):
        Library._who_reserve_book_dict.pop(book.book_title)
        Library._books_reserved.remove(book)

    @staticmethod
    def print_books_in_store():
        print("____________________________________")
        print("Список книг в наличии библиотеки")
        for i in Library._books_in_store:
            print(i.book_title)
        print("____________________________________")

    @staticmethod
    def print_books_reserved():
        print("____________________________________")
        print("Список зарезервированных книг")
        for i in Library._books_reserved:
            print(i.book_title)
        print("____________________________________")

    @staticmethod
    def get_books_in_store():
        return Library._books_in_store

    @staticmethod
    def get_who_took_book_dict():
        return Library._who_took_book_dict

    @staticmethod
    def get_who_reserve_book_dict():
        return Library._who_reserve_book_dict

    @staticmethod
    def add_initialized_book(book):
        Library._books_in_store.append(book)


class User:

    def __init__(self, name):
        self.name = name

    def take_book(self, book):
        if book in Library.get_books_in_store() and book not in Library.get_who_reserve_book_dict():
            Library.remove_book_from_storage(book, self)
        elif book not in Library.get_books_in_store():
            print(f"Книгу уже забрал пользователь с именем "
                  f"{Library.get_who_took_book_dict()[book.book_title]}")
        else:
            print(f"Книгу уже зарезервировал пользователь с именем "
                  f"{Library.get_who_reserve_book_dict()[book.book_title]}")

    def reserve_book(self, book):
        if book not in Library.get_who_reserve_book_dict() and book in Library.get_books_in_store():
            Library.add_book_to_reserved_list(book, self)
        elif book in Library.get_who_reserve_book_dict():
            print(f"Книгу уже зарезервировал пользователь с именем "
                  f"{Library.get_who_reserve_book_dict()[book.book_title]}")
        else:
            print(f"Книгу уже забрал пользователь с именем "
                  f"{Library.get_who_took_book_dict()[book.book_title]}")

    @staticmethod
    def cancel_reservation_of_book(book):
        Library.remove_book_from_reserved_list(book)

    @staticmethod
    def return_book(book):
        Library.add_book_to_storage(book)


user1 = User("Николай")
user2 = User("Павел")
book1 = Book("Книга1", "Жюль Верн", 500, "10101010101")
book2 = Book("Книга2", "Жюль Верн", 500, "10101010101")

Library.print_who_reserve_book_dict()
user1.take_book(book1)
Library.print_who_reserve_book_dict()
user2.reserve_book(book1)
Library.print_who_took_book_dict()
Library.print_who_reserve_book_dict()
