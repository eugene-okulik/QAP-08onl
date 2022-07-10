from test.book import Book

book1 = Book('Yesterday', 2015, 'Unknown Author2', 500)
book2 = Book('Today', 2022, 'Unknown Author1 ', 1100)
book3 = Book('Tomorrow', 2023, 'Unknown Author3', 1500)

print(book1.how_old())
print(book2.number_pages())
print(book3.how_old())
print(book3.number_pages())
print(book3.author)
print(book1.__dict__)
