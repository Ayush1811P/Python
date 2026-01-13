# num=int(input("Enter the number: "))
# is_prime=False
# if num <2:
#     print("not a prime number")
    
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             is_prime=False
#             break
#         else:               
#             is_prime=True
            
#     if is_prime==True:
#         print("It is a prime number!",num)
#     else:
#         print("It is not a prime number")




        # Q3️⃣
# Write a program to:
# Take a list of integers
# Count how many even and odd numbers are present
# Do NOT use built-in count function


# num=[]
# size=int(input("Enter the size of the list: "))
# for i in range(size):
#     value=int(input("Enter the element: "))
#     num.append(value)

# even=0
# odd=0
# for i in range(len(num)):
#     if num[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1

# print("Total even numbers are: ",even)    
# print("Total odd numbers are: ",odd)    

  



            # Q4️⃣ (Array + Logic)
# Write a program to:
# 🔹 Take a list of integers
# 🔹 Reverse the list without using slicing
# 🔹 Do NOT use reverse()


# list=[]
# size=int(input("Enter the size of the list: "))
# if size==0:
#     print("please enter size >= 1")
    
# else:

#     for i in range(size):
#         value=int(input("Enter the elements: "))
#         list.append(value)
#     print(list)

#     rev=[]
#     i=size-1
#     while i>=0:
#         values=list[i]
#         rev.append(values)
#         i-=1

#     print(rev)





            # Q5️⃣
# Write a program to:
# 🔹 Take a list of integers
# 🔹 Remove duplicate elements
# 🔹 Do NOT use set()
# 🔹 Preserve the original order


# num=[]
# size=int(input("Enter the size of the list: "))
# for i in range(size):
#     value=int(input("Enter the element: "))
#     num.append(value)


# num=[1, 2, 3, 2, 1, 4]
# print(num)    
# result=[]
# for i in num:
#     if i not in result:
#         result.append(i)

# print(result)            




            # Q6️⃣ 
# (Very Important — Exam & Interview Level)
# Write a program to:
# 🔹 Take a list of integers
# 🔹 Find the largest and smallest element
# 🔹 Do NOT use max() or min()


# arr=[12, 4, 56, 2, 89, 10]
# max=arr[0]
# min=arr[0]
# print(min)
# if len(arr)==1:
#     print("there is only one element")
#     print("it's itself max and min")
# else:
   
#     for i in arr:
        
#         if i>max:
#             max=i
#         if min>i:
#             min=i   

# print("MAX IS: ",max)             
# print("MIN IS: ",min)             




#             Q7️⃣
# (Functions + Binary Search)
# Write a function binary_search(arr, target) that:
# Takes a sorted list
# Returns the index if element is found
# Returns -1 if not found
# Do NOT use .index()


def is_binary(arr,target):
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid          
        else:
            if target <mid:
                end=mid-1
            else:
                start=mid+1    
    return -1


# arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# target=3
# result=is_binary(arr,target)
# print(result)

# def sum_ofAll(num):
#     if num==0:
#         return 0
#     return (num % 10) + sum_ofAll(num // 10)

# answer=sum_ofAll(1234)
# print(answer)


# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(b)
# print(a)




#              Q4️⃣ 
# (Coding | Lists + Loop + Condition)
# 👉 Task:
# Write a Python program that:
# Takes a list of numbers
# Creates a new list containing only even numbers
# Prints the new list


# old_list=[]
# size=int(input("Enter the size of the list: "))
# if size <=0:
#     print("Enter valid size number")
    
# else:
#     for i in range(size):
#         value=int(input("Enter the element: "))
#         if value<0:
#             print("please enter positive numbers")
#             continue
#         else:
#             old_list.append(value)

#     print(old_list)
#     even_list=[]

#     for i in old_list:
#         if i%2==0:
#             even_list.append(i)
#     print(even_list)
        





# data = {"a": 1, "b": 2}
# print(data)--