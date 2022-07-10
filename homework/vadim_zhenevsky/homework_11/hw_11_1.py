from utils.program import Book

first_book = Book('Властелин колец: Братство Кольца', 555, 'Дж. Р. Р. Толкин', 100)
second_book = Book('Сияние', 460, 'Стивен Кинг', 99)
third_book = Book('Зов Ктулху', 480, 'Г.Ф.Лавкрафт', 110)
print(first_book.is_long_book())
print(second_book.is_long_book())
print(first_book.is_cheap_or_not())
print(second_book.is_cheap_or_not())
print(third_book.book_info())
print(second_book.price)
print(third_book.pages)
print(third_book.name)
