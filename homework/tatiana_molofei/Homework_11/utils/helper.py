# В одном файле создайте класс. Класс должен содержать
# информацию о книге - класс Book. Атрибуты: количество страниц, год издания,
# автор, цена.

class Book:
    def __init__(self, pages, year, author, price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price

    def book_price(self):
        return 'expensive' if self.price > 30000 else 'cheap'

    def reading_time(self):
        return 'takes a lot of time to read' if self.pages > 1000 else 'read quickly'
