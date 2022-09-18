class Book:
    def __init__(self, autor, year_of_publication, pages, price):
        self.autor = autor
        self.year_of_publication = year_of_publication
        self.pages = pages
        self.price = price

    def information_book(self):
        return self.autor, self.year_of_publication, self.pages, self.price

    def get_autor(self):
        return self.autor

    def years(self):
        return f'Year of publication {self.year_of_publication}'

    def number_of_pages(self):
        return f'The book has {self.pages}pp.'

    def cost(self):
        return f'Price book: {self.price}$.'
