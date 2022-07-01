# Создайте папку с программой.
# В одном файле создайте класс, а команды, использующие этот класс поместите в другом файле.
#
# Класс должен содержать информацию о книге - класс Book.
# Атрибуты: количество страниц, год издания, автор, цена.
#
# В файле с командами создайте несколько экземпляров объекта Book.
# Для каждого из экземпляров выведите на экран какую-либо информацию о нем.
#
# Во время работы с импортом попробуйте разные способы
# (импорт конкретно класса, импорт файла, содержащего класс, и т.д.)

class Book:
    def __init__(self, name, year, price):
        self.name = name
        # self.pages = pages
        self.year = year
        # self.author = author
        self.price = price

    def is_expensive(self):
        return 'expensive' if self.price > 100 else 'cheap'

    def is_modern(self):
        return 'modern' if self.year > 2015 else 'classic'

    def overview(self):
        return self.name, self.year, self.price
