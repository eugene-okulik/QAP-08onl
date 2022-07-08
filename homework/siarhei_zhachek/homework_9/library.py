class Book:
    user = None
    reserve = False

    def __init__(self, title, author, pages, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id
        self.pages = pages

    def reserved(self, flag):
        self.reserve = flag

    def user_name(self, user):
        self.user = user


class User:
    def __init__(self, user_name):
        self.user_name = user_name

    @staticmethod
    def taken(book):
        if book.reserve is True:
            print('The book is currently reserved')
        elif book.user is not None:
            print('Now the book is being read')
        else:
            print('Will you take the book?')

    @staticmethod
    def reserve(book):
        book.reserved(True)
        return book.reserve


book1 = Book('Влястилин колец', 'Джон Р. Р. Толкин', 1120, '979-5-494-01620-1')
book2 = Book('Столпы Земли', 'Кен Фоллет', 880, '978-5-17-065893-0')
user1 = User('Олег')
user2 = User('Кля')
user3 = User('Вася')
user4 = User('Петя')
user1.reserve(book1)
user2.reserve(book2)
user3.taken(book2)
user4.taken(book1)
