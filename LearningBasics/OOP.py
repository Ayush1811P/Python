# #


# class Book:
#     def __init__(self, title, author, available=True):
#         self.title = title
#         self.author = author
#         self.available = available
#     def __str__(self):
#         return f"{self.title} by {self.author}"    

# Total_sales=0

# class Library:
#     def __init__(self):
#         self.books = []
        
#     def __str__(self):
#         return str(self.books)
#     def add_book(self, book, author):
#         book = Book(book, author)
#         self.books.append(book)
#         print(f"Book {book.title} added to the library.\n")
    
#     def issue_book(self,title,total_days):
#         self.total_days=total_days
#         for b in self.books:
#             if b.title.lower()==title.lower() and b.available:
#                 b.available = False
#                 print(f"Book {title} has been issued.\n")
                
#                 return 
#             print(f"Book {title} is Not Available \n")     
#             return 

#     def display_books(self):
#         if not self.books:
#             print("No book available in library")
#         else:
#             print("Books in the library:")
#             for b in self.books:
#                 print(f"{b.title} by {b.author}", end=" ")
#                 if b.available:
#                     print("Available")
#     def return_book(self,title,return_days):
#         self.return_days=return_days
#         for b in self.books:
#             if b.title.lower()==title.lower():
#                 if b.available:
#                     print(f"Book {title} is already in the library.\n")
#                     return
#                 else: 
#                     b.available=True
#                     print(f"Book {title} is Returned ")
#                     if self.total_days==self.return_days:
#                         self.Total_sales+=self.total_days*10
                        
#                     elif self.total_days-self.return_days >0:
#                         self.add=self.total_days-self.return_days
#                         self.add*=10
#                         self.Total_sales+=self.add
                        
#                     else:
#                        self.fine= self.return_days-self.total_days
#                        self.fine=self.fine*10
                       
#                        self.Total_sales+=self.fine
#                     return 

# Lib=Library()
# Lib.add_book("AIR","AYUSH")
# Lib.add_book("FIRE","AYU")

# print("1: Add Book\n2: Issue Book\n3: Display all books\n4: Return Boook\n5:Account Info \n6 Exit")
# while True:
    
#     choice=int(input("\n\tEnter your choice: "))
#     match choice:
#         case 1:
#             try:

#                 book_name=input("Enter Book Title: ")
#                 author_name=input("Author Name: ")
#                 Lib.add_book(book_name,author_name)
#             except ValueError:
#                 print(-1)    
#         case 2:
#             try:

#                 print("10 Rupees for 1 day\n")
#                 book_name=input("Enter book name: ")
#                 days=int(input("For how many days?: "))
#                 Lib.issue_book(book_name,days)
#             except ValueError:
#                 print(-1)    
#         case 3:
#             try:
#                 Lib.display_books()
#             except ValueError:
#                 print(-1)    
                  
#         case 4:
#             try:

#                 book_name=input("Enter book name to Return: ")
#                 days=int(input("total days kept book : "))
#                 Lib.return_book(book_name,days)
#             except ValueError:
#                 print(-1)    
#         case 5:
#             try:

#                 print("Total Sales:",Lib.Total_sales  ) 
#             except ValueError:
#                 print(-1)    
#         case 6:
#             break
                 






class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.days = 0   

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []
        self.Total_sales = 0   

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added.\n")

    def issue_book(self, title, days):
        for b in self.books:
            if b.title.lower() == title.lower() and b.available:
                b.available = False
                b.days = days
                print(f"Book '{title}' issued for {days} days.\n")
                return
        print(f"Book '{title}' not available.\n")

    def return_book(self, title, return_days):
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.available:
                    print(f"Book '{title}' already in library.\n")
                    return

                b.available = True
                print(f"Book '{title}' returned.\n")

                
                if return_days <= b.days:
                    self.Total_sales += return_days * 10
                else:
                    extra = return_days - b.days
                    self.Total_sales += (b.days * 10) + (extra * 10)
                return

        print(f"Book '{title}' not found.\n")

    def display_books(self):
        if not self.books:
            print("No books available\n")
        else:
            for b in self.books:
                print(b)
            print()

    def show_sales(self):
        print("Total Sales:", self.Total_sales, "\n")


Lib = Library()

Lib.add_book("AIR", "AYUSH")
Lib.add_book("FIRE", "AYU")

while True:
    print("1.Add  2.Issue  3.Display  4.Return  5.Sales  6.Exit")
    try:
        ch = int(input("Enter choice: "))

        if ch == 1:
            t = input("Title: ")
            a = input("Author: ")
            Lib.add_book(t, a)

        elif ch == 2:
            t = input("Title: ")
            d = int(input("Days: "))
            Lib.issue_book(t, d)

        elif ch == 3:
            Lib.display_books()

        elif ch == 4:
            t = input("Title: ")
            d = int(input("Return days: "))
            if d<0:
                print("Invalid Input\n")
            Lib.return_book(t, d)

        elif ch == 5:
            Lib.show_sales()

        elif ch == 6:
            break

    except:
        print("Invalid input\n")