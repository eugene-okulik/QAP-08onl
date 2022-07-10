class Book:
    def __init__(self, pages, year, author, price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price

    def book_price(self):
        return 'не дорого' if self.price < 2000 else 'дорого'

    def reading_time(self):
        return 'Читается долго' if self.pages < 1000 else '  Читается на одном дыхании'
