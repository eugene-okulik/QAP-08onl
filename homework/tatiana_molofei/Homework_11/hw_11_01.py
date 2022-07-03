# Импорт класса
# Создайте папку с программой. В одном файле создайте класс, а команды,
# использующие этот класс поместите в другом файле. Класс должен содержать
# информацию о книге - класс Book. Атрибуты: количество страниц, год издания,
# автор, цена. В файле с командами создайте несколько экземпляров объекта Book.
# Для каждого из экземпляров выведите на экран какую-либо информацию о нем.
# Во время работы с импортом попробуйте разные способы (импорт конкретно класса,
# импорт файла, содержащего класс, и т.д.)

from utils.helper import Book

book1 = Book(550, 2005, 'Ray Bradbury', 1800)
book2 = Book(350, 1980, 'Charles Dickens', 2500)
book3 = Book(1500, 2004, 'Gabriel Garcia Marquez', 2800)
book4 = Book(300, 2015, 'Antoine de Saint-Exupéry', 35000)


def book_info(self):
    return self.pages, self.year, self.authour, self.price


print(f'Book price is {book1.price} rubles')
print(f'Book author is {book2.author}')
print(f'Book has {book3.pages} pages')
print(f'The book was published in {book4.year} year')
