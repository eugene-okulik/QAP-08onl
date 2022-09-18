from program.class_of_program import Book

first_book = Book('Портрет Дориана Грея', 552, 'Оскар Уайльд', 100)
second_book = Book('Мальчик-звезда', 450, 'Оскар Уайльд', 90)
third_book = Book('Эгоистичный великан', 490, 'Оскар Уайльд', 110)
print(first_book.is_long_book())
print(second_book.is_long_book())
print(first_book.is_cheap_or_not())
print(second_book.is_cheap_or_not())
print(third_book.book_info())
print(second_book.price)
print(third_book.pages)
print(third_book.name)
