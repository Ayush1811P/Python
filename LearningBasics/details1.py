# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True
#     def __str__(self):
#         return f"{self.title} by {self.author}"   

# class Library:
#     def __init__(self):
#         self.books = []
#         print(self.books)
#     def add_book(self, title, author):
#         self.books.append(Book(title, author))
        

#     def display_books(self):
#         if not self.books:
#             print("No books in the library.")
#         else:
#             print("Books in the library:")
#             for book in self.books:
#                 print(book)




# # b1=Book("Aviator in the sky","Phill Salt")
# l1=Library()
# l1.add_book("Aviator in the sky","Phill Salt")
# l1.add_book("Falling from the sky","Glenn Phillips")
# print(l1.display_books())




#2-> FIZZ
#3-> BUZZ
# both=[]
# Even=[]
# Odd=[]

# for i in range(int(input("Enter starting: ")),int(input("Enter Ending: "))):
#     if i%2==0 and i%3!=0: 
#         Even.append(i)
#     elif i%2==0 and i%3==0:
#         both.append(i)    
#     elif i%3==0:
#         Odd.append(i)
        
# print(f"Even: {tuple(Even)}\n ODD: {tuple(Odd)}\n Both: {both}")            







# prime number
# num=int(input("Enter number: ")) 
# isprime=True
# if num<=0:  #1
#     print("Enter a positive number")
#     isprime=False

# if num==1: #2
#     print("Not a prime number")
#     isprime=False
# for i in range(2,num):
#     #ITERATIVE CONDITIONS #3
#     if num % i==0:  
#         print("Not a prime number")
#         isprime=False
#         break
#     else:
#         pass
# if isprime==True:
#     print("Prime number") 

   

#ITERATION 9-1==8
#NUM = 9
#2-> 2%9==0
#3-> 3%==0  T

"""IN THE GIVEN LIST
PRINT LIST OF EVEN, ODD, PRIME NUMBERS 
WITHOUT USING PRE DEFINED FUNC()

"""
# L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# even =[]
# odd =[]
# prime =[]
# for i in L:
#     if i%2==0:
#         even.append(i)
#     if i%3==0:
#         odd.append(i)
#     if i<=1:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break  
#     else:
#         prime.append(i)#3<- 5<- 7<- 
# print("PRIME: ",prime)            
# print("ODD: ",odd)            
# print("Even: ",even)            
          