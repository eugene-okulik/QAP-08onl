class Book:
    def __init__(self, pages, publishing, author, price):
        self.pages = pages
        self.publishing = publishing
        self.author = author
        self.price = price

    def book_pages(self):
        if self.pages < 500:
            return 'few pages'
        return 'many pages'

    def book_publishing(self):
        if self.publishing > 2010:
            return 'new'
        return 'old book'

    def book_price(self):
        if self.price < 30:
            return 'cheap'
        return 'expensive'
