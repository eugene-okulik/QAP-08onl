from package.book import Book

book1 = Book('New Tales', 2020, 150)
book2 = Book('Old Tales', 1980, 90)

print(book1.is_expensive())
print(book2.is_modern())
print(book1.__dict__)
print(book1.price)
