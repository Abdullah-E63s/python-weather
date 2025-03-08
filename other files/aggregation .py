class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def list_books(self):
        return [f"{book.title} by  {book.author} " for book in self.books]

    def add_book(self, book):
        self.books.append(book)
        

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

library = Library("London Public Library")

book1 = Book("Harry potter.....", "J.k .Rowling")
book2 = Book("The Hobbit", "R. R. Tolkin")
book3 = Book("The Colour of Magic", " Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print(library.name)
# print(library.list_books())
for book in library.list_books():
    print(book)