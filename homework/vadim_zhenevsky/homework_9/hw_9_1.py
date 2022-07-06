class Book:
    reserved = False
    user = None

    def __init__(self, name, isbn, pages, author):
        self.name = name
        self.isbn = isbn
        self.pages = pages
        self.author = author

    def set_reserve(self, value):
        self.reserved = value

    def set_user(self, user):
        self.user = user


class User:
    @staticmethod
    def reserve(book):
        book.set_reserve(True)

    def get_book(self, book):

        if book.user is not None or book.reserved is True:
            print("Нельзя взять книгу")
        else:
            print("Можно взять книгу", book.name)
            book.set_user(self)

    @staticmethod
    def return_book(book):
        book.set_user(None)


book1 = Book("Людзі на балоце", "134527", 300, "Іван Мележ")
book2 = Book("Война и Мир", "234569", 320, "Л. Н. Толстой")
book3 = Book("Гарри Поттер и философский камень", "239874", 490, "Дж.К. Роулинг")

user1 = User()
user2 = User()
user3 = User()

user1.reserve(book1)
user2.get_book(book2)
user3.get_book(book1)
user1.get_book(book2)
user2.return_book(book2)
user1.get_book(book2)
user3.reserve(book3)
