class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def register(self, patron):
        self.patrons.append(patron)
        print("Patron registered")

    def borrow(self, name):
        for b in self.books:
            if b.name == name and b.available:
                b.available = False
                print("Book borrowed:", name)
                return
        print("Book not available")

    def return_book(self, name):
        for b in self.books:
            if b.name == name:
                b.available = True
                print("Book returned:", name)
                return

lib = Library()

b1 = Book("Python", "Guido")
p1 = Patron("Aryan")

lib.add_book(b1)
lib.register(p1)
lib.borrow("Python")
lib.return_book("Python")
