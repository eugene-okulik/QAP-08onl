# В одном файле создайте класс. Класс должен содержать
# информацию о книге - класс Book. Атрибуты: количество страниц, год издания,
# автор, цена.

class Book:
    def __init__(self, pages, year, author, price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price
