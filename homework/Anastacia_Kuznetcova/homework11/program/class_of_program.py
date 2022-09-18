class Book:
    def __init__(self, name, pages, author, price):
        self.name = name
        self.pages = pages
        # self.year = year
        self.author = author
        self.price = price

    def is_long_book(self):
        return 'Длинная книга' if self.pages > 550 else 'Короткая книга'

    def is_cheap_or_not(self):
        return 'Дорогая книга' if self.price > 90 else 'Дешевая книга'

    def book_info(self):
        return self.name, self.pages, self.author, self.price
