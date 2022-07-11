from ht1 import Book

book1 = Book(450, 1999, 'Stephen King', 25)
book2 = Book(516, 2012, 'Ian Fleming', 36)
book3 = Book(710, 2008, 'Charles Bukowski', 17)
book4 = Book(250, 2019, 'Harriet Doerr', 40)


def book_info(self):
    return self.pages, self.publishing, self.author, self.price


print(f'Number of pages in this book - {book1.pages}')
print(f'This book was published in {book2.publishing} year')
print(f'The author of this book is {book3.author}')
print(f'The price of this book is {book4.price} rubles')
print(f'The book {book1.author} is {book1.book_publishing()}')
print(f'The book {book2.author} is {book2.book_price()}')
print(f'The book {book4.author} is {book4.book_publishing()}')
print(f'The book {book3.author} is {book3.book_price()}')
print(f'The book {book1.author} has {book1.book_pages()}')
print(f'The book {book3.author} has {book3.book_pages()}')
