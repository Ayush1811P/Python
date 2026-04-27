# Class representing a Book
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.available else 'Issued'}"

# Class representing a Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"Book '{title}' has been issued.")
                return
        print(f"Book '{title}' is either not available or already issued.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)