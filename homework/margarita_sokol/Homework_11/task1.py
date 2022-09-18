# Создайте папку с программой.
# В одном файле создайте класс, а команды,
# использующие этот класс поместите в другом файле.
# Класс должен содержать информацию о книге - класс Book.
# Атрибуты: количество страниц, год издания, автор, цена.
# В файле с командами создайте несколько экземпляров объекта Book.
# Для каждого из экземпляров выведите на экран какую-либо информацию о нем.
# Во время работы с импортом попробуйте разные способы
# (импорт конкретно класса, импорт файла, содержащего класс, и т.д.)

from utils.helper import Book

book1 = Book(1800, 1959, 'Erich Maria Remarque', 16000)
book2 = Book(1000, 2021, 'Freya Sampson', 10000)
book3 = Book(2000, 1966, 'Daniel J. Keys ', 20000)
book4 = Book(1100, 2019, 'Mary Burton', 15000)

print(f'Book has {book1.pages} pages')
print(f'The book was published in {book2.year} year')
print(f'Book author is {book3.author}')
print(f'Book price is {book4.price} rubles')
print(f'The book {book1.author} is {book1.reading_time()}')
print(f'The book {book2.author} is {book2.reading_time()}')
print(f'The book {book3.author} is {book3.book_price()}')
print(f'The book {book4.author} is {book4.book_price()}')
