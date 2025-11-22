# Aggregation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Usage
b1 = Book("Python 101", "Saed")
b2 = Book("Learn OOP", "Abu")
lib = Library("City Library")
lib.add_book(b1)
lib.add_book(b2)
lib.show_books()