class Book:
    def __init__(self, name, year, author, quantity):
        self.__name = name
        self.__year = year
        self.__author = author
        self.__quantity = quantity

    @property
    def info(self):
        return self.__name, self.__year, self.__author, self.__quantity

    @info.deleter
    def info(self):
        del self.__name, self.__year, self.__author, self.__quantity

    def update_quantity(self, quan):
        self.__quantity = quan
