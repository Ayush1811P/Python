# # -------------------- 1. Quotient & Remainder --------------------
# # print("PROGRAM 1")
# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))
# # q = a // b
# # r = a - (b * q)
# # print("Quotient:", q)
# # print("Remainder:", r)





# # # -------------------- 2. Swap --------------------
# # print("\tPROGRAM 2")
# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))
# # a = a + b
# # b = a - b
# # a = a - b
# # print("After swap:", a, b)


# # # -------------------- 3. Count occurrences --------------------
# # print("\tPROGRAM 3")
# # lst = [2, 3, 2, 5, 2, 8]
# # x = int(input("Enter element to count: "))
# # count = 0
# # for i in lst:
# #     if i == x:
# #         count += 1
# # print("Count:", count)


# # # -------------------- 4. Max & Min --------------------
# # print("\tPROGRAM 4")
# # lst = [4, 12, 7, 1, 19, 8,0, 3]
# # maxi = lst[0]
# # mini = lst[0]
# # for i in lst:
# #     if i > maxi:
# #         maxi = i
# #     if i < mini:
# #         mini = i
# # print("Max:", maxi)
# # print("Min:", mini)


# # # -------------------- 5. Remove duplicates --------------------
# print("\tPROGRAM 5")
# lst =[23,45,7,2,4,6,10,5,35,16,12]  

# num = int(input("enter num:"))
# idx = int(input("index:"))
# for i in range(len(lst)):
#     print(i)
#     if i == idx:
    
#        lst.insert(idx,num)
#        break
# print(lst)     
# lst.insert(idx,num)
# print(lst)

# lst =[23,34,1,3,12,67,30,5,15]
# print(lst)
# num = int(input("enter num:"))
# idx = int(input(input(("index:"))))
# for i in range (len(lst)):
#     if i == idx:
#         lst.insert(idx,num,idx,num)
#         break
# print(lst)
# import random

# password=0

# password=random.randint(111,999)
# char="abcdefghijklmnopqrstuvwxyz"
# for i in range(3):
#     password=str(password)+random.choice(char)

# print(password)




# for i in range (len(lst)):
#     if n==i:
#        print(lst.index(i))
    
# if n in lst:
#     print(n,"yes no is found")
# else:
#     print(n,"not found")    




# print(len(lst))
# size= len(lst)//2
# lst2=[]
# for i in range (size):
#     lst2.append(lst[i])
# print(lst2)

# even=0
# odd=0
# for i in lst:
#     if i%2==0:
#         even += 1
#     else:
#         odd +=1    
# print(even,"total even no.")
# print(odd,"total odd no.")






# # # -------------------- 6. List ↔ Tuple --------------------
# # print("\tPROGRAM 6")
# # lst = [1, 2, 3, 4]
# # t = ()
# # for i in lst:
# #     t = t + (i,)
# # print("Tuple:", t)

# # lst2 = []
# # for i in t:
# #     lst2.append(i)
# # print("List:", lst2)


# # # -------------------- 7. Char frequency --------------------
# # print("\tPROGRAM 7")
# # s = input("Enter string: ")
# # d = {}
# # for ch in s:
# #     if ch in d:
# #         d[ch] += 1
# #     else:
# #         d[ch] = 1
# # print(d)


# # # -------------------- 8. Count digits --------------------
# # print("\tPROGRAM 8")
# # n = int(input("Enter number: "))
# # c = 0
# # while n != 0:
# #     n //= 10
# #     c += 1
# # print("Digits:", c)


# # # -------------------- 9. Search element --------------------
# # print("\tPROGRAM 9")
# # lst = [10, 20, 30, 40, 50]
# # x = int(input("Enter element to search: "))
# # for i in range(len(lst)):
# #     if lst[i] == x:
# #         print("Found at index", i)
# #         break
# # else:
# #     print("Not found")


# # # -------------------- 10. Function --------------------
# # print("\tPROGRAM 13")
# # def add(a, b):
# #     return a + b

# # x = int(input("Enter a: "))
# # y = int(input("Enter b: "))
# # print("Sum:", add(x, y))


# # # -------------------- 11. Lambda --------------------
# # print("\tPROGRAM 11")
# # lst = [1, 2, 3, 4]
# # res = list(map(lambda x: x * x, lst))
# # print(res)


# # # -------------------- 12. OTP --------------------
# # print("\tPROGRAM 13")

# # otp = "1256"

# # print("Random OTP:", otp)


# # # -------------------- 13. Package (basic) --------------------


# # # -------------------- 14. Class --------------------
# # print("\tPROGRAM 15 \n\tCLASS & OBJECT")
# # class A:
# #     def show(self):
# #         print("Hello")
# # obj = A()
# # obj.show()


# # # -------------------- 15. Constructor --------------------
# # print("\tPROGRAM 15")
# # class B:
# #     def __init__(self):
# #         print("Constructor")
# #     def __del__(self):
# #         print("Destructor")
# # obj = B()
# # del obj


# # # -------------------- 16. Multilevel --------------------
# # print("\tPROGRAM 1\n\tMultilevel")
# # class X:
# #     def f1(self): print("A")
# # class Y(X):
# #     def f2(self): print("B")
# # class Z(Y):
# #     def f3(self): print("C")
# # obj = Z()
# # obj.f1(); obj.f2(); obj.f3()


# # # -------------------- 17. Overloading --------------------
# # print("\tPROGRAM 17\n\t Overloading")
# # class C:
# #     def add(self, a=None, b=None):
# #         if a and b:
# #             print(a + b)
# #         else:
# #             print("Need 2 values")
# # obj = C()
# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))
# # obj.add(a, b)


# # # -------------------- 18. Polymorphism --------------------
# # print("\tPROGRAM 18\n\t Polymorphism")
# # class D:
# #     def show(self): print("A")
# # class E(D):
# #     def show(self): print("B")
# # obj = E()
# # obj.show()


# # # -------------------- 19. Exception --------------------
# # print("\tPROGRAM 19\n\t Exception")
# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))
# # try:
# #     print(a / b)
# # except:
# #     print("Error")


# # # -------------------- 20. Raise --------------------
# # print("\tPROGRAM 20\n\t Raise")
# # a = int(input("Enter number: "))
# # if a < 0:
# #     raise Exception("Negative not allowed")
# # print(a)


# # # -------------------- 21. MySQL connect --------------------
# # import mysql.connector
# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="",
# #     database="test"
# # )
# # print("Connected")


# # # -------------------- 22. Insert --------------------
# # cur = db.cursor()
# # a = int(input("Enter id: "))
# # b = input("Enter name: ")
# # cur.execute("insert into student values(%s,%s)", (a,b))
# # db.commit()
# # print("Inserted")


# # # -------------------- 23. Word frequency --------------------
# # print("\tPROGRAM 23\n\t Word frequency")
# # s = input("Enter sentence: ")
# # words = s.split()
# # d = {}
# # for w in words:
# #     if w in d:
# #         d[w] += 1
# #     else:
# #         d[w] = 1
# # print(d)


# # # -------------------- 24. First repeating char --------------------
# # print("\tPROGRAM 24\n\t First repeating char")
# # s = input("Enter string: ")
# # for i in range(len(s)):
# #     for j in range(i+1, len(s)):
# #         if s[i] == s[j]:
# #             print("First repeat:", s[i])
# #             break
# #     else:
# #         continue
# #     break


# # # -------------------- 25. Linear search --------------------
# # print("\tPROGRAM 25\n\t Linear search")
# # lst = [5, 10, 15, 20]
# # x = int(input("Enter element: "))
# # for i in range(len(lst)):
# #     if lst[i] == x:
# #         print("Index:", i)


# # # -------------------- 26. Hangman --------------------
# print("\tPROGRAM 26\n\t ")
# import random
# words = ["python", "yrogramming", "words", "jyush", "gaurav", "priyansh"]
# lives = 6
# print("Welcome to Hangman!")

# while lives > 0:
#     chosen_word = random.choice(words)
#     guess = input("Guess a character: ").lower()

#     if len(guess) != 1:
#         print("enter one character only")

#     if guess in chosen_word:
#         print("Correct guess!\nComputer choice was:", chosen_word)
#         break
#     else:
#         lives -= 1
#         print("_" * len(chosen_word))
#         print("Wrong guess! Lives left:", lives)

#     if lives == 0:
#         print("Game over! The word was:", chosen_word)

# S="Ayush  "
# U=input("Enter username: ").upper()
# if U.strip()==S.upper().strip():
#     print("PASS")
# else:
#     print("FAIL")





# S="Ay2u4s5h1811"
#  #1

# S2=""
# S3=""
# for i in S:
#     if i.isalpha():
#         S2+=i
#     else:
#         S3+=i
# print("Prev: ",S,"\nAfter: ",S2,"\nDigits: ",S3)        


# def first_unique_word(sentence):
#     freq={}
#     for ch in sentence.split():
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#     for keys,values in freq.items():
#         if values==1:
#             return f"First Unique sentense is : {keys}"
#     return f"no unique item found!"        

# print(first_unique_word("this this is is a a test test"))


       # QUESTION 1
# def product_except_self(nums):
#     res=[]
#     curr=0
#     val=1
#     while curr<len(nums):
#         for j in range(len(nums)):
#             if j!=curr:
#                 val=val*nums[j]
#         res.append(val)
#         val=1
#         curr+=1        
#     return res

# print( product_except_self([2,2,2,3,4]))



    # QUESTION 2
# def top_k_frequent(nums,k):
#     freq={}
#     res=[]
#     for i in nums:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     freq=dict(sorted(freq.items(), key = lambda item: item[1],reverse=True))
#     i=1
#     for key,value in freq.items():
#         res.append(value)
#         if i==k:
#             break
#         i+=1
#     return res
    
# print(top_k_frequent([3,4,1,1,1,1,2,2,2,2,2,1,2],2))   




        # QUESTION 3
# def first_missing_positive(nums):
#     positive=1
#     nums=sorted(nums)
#     for i in nums:
#         if i==positive:
#             positive+=1
        
#     return print("the first positive number missing is ",positive)
            

# first_missing_positive([-1,1,3,4,5,7])


# a=[5,3,8,3,9,3]
# a.remove(3)
# x=a.pop(2)
# a.append(x + 1)
# print(a)
# print(len(a))



# a=int(input("Enter number: "))
# b=int(input("to find percentage:  "))
# c=a//10
# d=b//10
# percentage=c*d
# print(f"{b} Percentage of {a} is ->{percentage}")