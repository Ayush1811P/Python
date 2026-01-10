# def add(a,b):     # creation and declaration of 
#     print(a+b)     # output of the function is called
# add(10,12)        #calling function
    


# def gteet(name="guest"):
#     print("Hello",name)

# result=gteet("Aayuu")  



# def square(n):
#     return n * n
# result=square(5)
# print(result)




        #1️⃣ Write a function to check even or odd
# def odd_even(*nums):
    
#     odd=0
#     even=0
#     for n in nums:
#         if n%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     return odd,even   
#print(odd_even(12,14,13,15,16,17))    



#2️⃣ Write a function that returns maximum of 3 numbers
# def max(a,b,c):
#     max=0
#     if a > b and a>c:
#         max=a
#     elif b>a and b>c:
#         max=b
#     else:
#         max=c        
#     return max    

# result=max(12,15,14)
# print(result)


#3️⃣ Use *args to add unlimited numbers
# def add_unlimited(*nums):
#     print(nums)

# result=add_unlimited(1,2,3,3,34,24,34,5)
# print(result)



#✅ Problem 8: Factorial
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact    

# print(factorial(5))



#✅ Problem 9: Count Vowels

# def count_vowels(s):
#     count=0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count +=1
#     return count        

# print(count_vowels("PYTHONAYUSHENGLISH"))








        #MAKING A PROGRAM USING FUNCTION DECLERATION AND CALLING
# def calculator():
#     print("Welcome to the calculator!")
#     num1=int (input("Enter num1: "))
#     num2 =int (input("Enter num2: "))
#     operator = input("enter operator: ")
#     match operator:
#         case "+":
#             print(num1+num2)
#         case "-":
#             print(num1-num2)
#         case "*":
#             print(num1*num2)
#         case "/":
#             if num2 != 0:
#                 print(num1/num2)
#             else:
#                 print("division not possible")

#         case "%":
#             print(num1%num2)
            

# def factorial():
#     num = int (input("enter the number: "))
#     fact=1
#     for i in range(1, num+1):
#         fact*=i 
#     print("Factorial of: ",fact)    


# def evenOdd():
#     num=int(input("enter the number: "))
#     if num%2==0:
#         print("the number is Even")
#     else:
#         print("the number is odd")


# print("call calculator 1")
# print("call even\odd  2")
# print("call factorial  3")
# choice = int (input("enter choice"))
# if choice ==1:
#     calculator()
# elif choice == 2:
#     evenOdd()
# elif choice==3:
#     factorial()
# else:
#     exit()



# def add(a,b):
#     return a+b
# sum = add(10,10)
# print(sum)


      
# def sub(a,b):
#     return a-b
# print(sub(10,5))



# def power (base, exp=2):
#     return base ** exp

# print(power(5))
# print(power(5,3))

    

        #VARIABLE LENGTHS ARGUMENTS
# def add_all(*nums):
#     total =0
#     for n in nums:
#         total += n
#     return total
# print(add_all(1,2,3,4))    



