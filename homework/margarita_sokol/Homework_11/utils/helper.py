class Book:
    def __init__(self, pages, year, author, price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price

    def info(self):
        return self.pages, self.year, self.author, self.price

    def reading_time(self):
        return 'read for a long time' if self.pages > 1200 else 'read quickly'

    def book_price(self):
        return 'this is expensive book' if self.price > 15000 else 'this is cheap book'
