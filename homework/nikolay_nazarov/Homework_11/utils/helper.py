class Book:
    def __init__(self, page_num, year_of_publication, author, price):
        self.page_num = page_num
        self.year_of_publication = year_of_publication
        self.author = author
        self.price = price

    def get_page_num(self):
        return self.page_num
