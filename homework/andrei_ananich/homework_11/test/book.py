# Создайте папку с программой.
# В одном файле создайте класс, а команды, использующие этот класс поместите в другом файле.
# Класс должен содержать информацию о книге - класс Book.
# Атрибуты: количество страниц, год издания, автор, цена.
# В файле с командами создайте несколько экземпляров объекта Book.
# Для каждого из экземпляров выведите на экран какую-либо информацию о нем.
# Во время работы с импортом попробуйте разные способы
# (импорт конкретно класса, импорт файла, содержащего класс, и т.д.)

class Book:
    def __init__(self, name, year, author, pages):
        self.name = name
        self.year = year
        self.author = author
        self.pages = pages

    def how_old(self):
        return 'This is old' if self.year < 2017 else 'This is new book'

    def number_pages(self):
        return 'This is long read' if self.pages > 1000 else 'This is quick read'

    def info(self):
        return self.name, self.year, self.author, self.pages
