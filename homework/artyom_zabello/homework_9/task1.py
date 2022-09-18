class Book:
    def __init__(self, name, author, reserved_flag=False, store_flag=True):
        self._name = name
        self._author = author
        self._reserved_flag = reserved_flag
        self._store_flag = store_flag

    def book_info(self):
        """Returns information about whether the book is booked and whether it is
         in the store or was it taken away. Accepts an object of the book class as input """
        if not self._reserved_flag:
            res = f"The book {self._name} is not reserved"
        else:
            res = f"The book {self._name} is reserved"
        if self._store_flag:
            res2 = f"The book {self._name} is in the store"
        else:
            res2 = f"The book {self._name} is not in the store"
        return f"{res}, {res2}"

    @property
    def book(self):
        return self._name

    @property
    def flag_store(self):
        return bool(self._store_flag)

    @property
    def flag_reserve(self):
        return self._reserved_flag

    def booking(self, operation, user):
        """This is a function for booking. She receives an operation
        code at the input(True/False) and changes the flag depending on it"""
        if operation and not self._reserved_flag:
            setattr(self, '_reserved_flag', True)
            return print(f"The book {self._name} was reserved by {user}")
        if not operation and self._reserved_flag:
            setattr(self, '_reserved_flag', False)
            return print(f"The reservation was cancelled at book {self._name} by {user}")
        raise ValueError("Operation is incorrect")

    def get_book(self, operation, user):
        """This is a function for get books at home. She receives an operation
                code at the input(True/False) and changes the flag depending on it"""
        if operation:
            setattr(self, '_store_flag', False)
            return print(f"The user {user} took the book {self._name}")
        if not operation:
            setattr(self, '_store_flag', True)
            return print(f"The user {user} returned the book {self._name}")
        raise ValueError("Operation is incorrect")


class User:
    def __init__(self, user_name):
        self.books = {}
        self.reserved_books = {}
        self.user_name = user_name

    @property
    def get_user(self):
        return self.user_name

    def book_a_book(self, book_name):
        """This function gives a possibility
        to book a book as a user.Gets an object of the book class as input"""
        if book_name.book not in self.books and bool(book_name.flag_store) and \
                not bool(book_name.flag_reserve):
            self.reserved_books = {book_name.book: self.user_name}
            book_name.booking(True, self.user_name)
        else:
            print("The book is already reserved or located at user")

    def read_a_book(self, book_name):
        """This function gives a possibility
        to get book as a user.Gets an object of the book class as input"""
        if book_name.book not in self.books and bool(book_name.flag_store) and \
                not bool(book_name.flag_reserve):
            self.books = {book_name.book: self.user_name}
            book_name.get_book(True, self.user_name)
        else:
            print("The book is already reserved or located at user")

    def cancel_reservation(self, book_name):
        """Cancellation of booking as a user.
        Gets an object of the book class as input"""
        if book_name.book in self.reserved_books:
            self.reserved_books.clear()
            book_name.booking(False, self.user_name)

    def return_book(self, book_name):
        """Returning of books as a user.
        Gets an object of the book class as input"""
        if book_name.book in self.books:
            self.books.clear()
            book_name.get_book(False, self.user_name)


book1 = Book('War and peace', 'Pushkin')
book2 = Book('Fighting club', 'Palanik')

user1 = User("Вася")
user2 = User("Жорик")

user1.book_a_book(book1)
user2.read_a_book(book2)
print(user1.reserved_books)
print(user2.books)
user1.cancel_reservation(book1)
user2.return_book(book2)
print(user1.reserved_books)
print(user2.books)
