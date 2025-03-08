class Book:
    def __init__(self, title, aurthor, num_pages):
        self.title = title
        self.author = aurthor
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}', by {self.author} with {self.num_pages} pages"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'number of pages':
            return self.num_pages
        else :
            return f"{key} was not found"

book1  = Book("The Hobbit", "J.R.R Tolkien", 320)
book2  = Book("Harry potter and the  philosphers stone", "J.K Rowling", 223)
book3  = Book("The Lion, the witch and wardrobe", "C.S Lewis", 172)

print(book1)
print(book1 == book2)
print(book2 < book3)
print(book1 > book2)
print(book1 + book3) 
print("Lion" in book3)
print(book3 ['au'])
