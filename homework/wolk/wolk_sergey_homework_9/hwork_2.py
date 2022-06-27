class Book:

    def __init__(self, author: str, publishing: int, title: str):
        self.author, self.publishing, self.title = author, publishing, title

    def __repr__(self) -> str:
        return f"{self.author}: \"{self.title}\" [{self.publishing} г.]"


class Library:

    def __init__(self, *book_1: Book):
        self.books = list(book_1)

    def append_book(self, book_3: Book):
        self.books.append(book_3)

    def remove_book(self, book_3: Book):
        self.books.remove(book_3)

    def find_books(self, **options: any) -> [Book]:
        books_2 = []
        for book_7 in self.books:
            for option, value in options.items():
                if getattr(book_7, option) != value:
                    break
            else:
                books_2.append(book_7)
        return books_2

    def sort_books(self, option: str, reverse: bool = False):
        self.books.sort(key=lambda book_4: getattr(book_4, option), reverse=reverse)


home_library = Library(
    Book("Эрик Мэтиз", 2019, "Изучаем Python. "
                             "Программирование игр, визуализация данных, веб-приложения")
)

home_library.append_book(
    Book("Пол Бэрри", 2015, "Изучаем программирование на Python")
)

print(home_library.books)
print(home_library.find_books(author="Пол Бэрри"))
print(home_library.find_books(publishing=2019))

home_library.sort_books("author", True)
print(home_library.books)

books = home_library.find_books(title="Изучаем Python. "
                                      "Программирование игр, визуализация данных, веб-приложения")
for book in books:
    home_library.remove_book(book)

print(home_library.books)
