class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def __str__(self):
        return f"{self.title} by {self.author}"   

class Library:
    def __init__(self):
        self.books = []
        print(self.books)
    def add_book(self, title, author):
        self.books.append(Book(title, author))
        

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)




# b1=Book("Aviator in the sky","Phill Salt")
l1=Library()
l1.add_book("Aviator in the sky","Phill Salt")
l1.add_book("Falling from the sky","Glenn Phillips")
print(l1.display_books())