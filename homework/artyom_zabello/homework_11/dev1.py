from test_pack.book import Book

book1 = Book('Game of thrones', 1984, 'J.Martin', 11)
book2 = Book('1984', 1961, 'G.Orwell', 15)

print(book1.info)
book2.update_quantity(18)
print(book2.info)
del book1.info
print(book1.__dict__)
