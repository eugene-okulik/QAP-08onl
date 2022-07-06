from utils.helper import Book

book1 = Book(550, 1901, 'Мастер и Маргарита', 1500)
book2 = Book(350, 1980, 'Шантарам', 3500)
book3 = Book(950, 2004, 'Три товарища', 900)
book4 = Book(520, 2014, 'Цветы для Элджернона', 5500)
book5 = Book(630, 2005, 'Портрет Дориана Грея', 6500)

def book_info(self):
    return self.pages, self.author, self.price, self.year


def book_price(self):
    return 'не дорогая' if self.price > 2000 else 'дорогая'


print(f'Цена книги {book4.price} тугриков')
print(f'В книге {book4.pages} страниц')
print(f'Книга опубликована в {book4.year} году')
print(f'Книга {book4.author}  {book4.book_price()}')
print(f'Книга {book4.author}  {book4.reading_time()}')
