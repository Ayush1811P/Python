# list=[]
# size=int(input("Enter the size of the list: "))
# for i in range (0,size):
#     value=input("Enter the value: ")
#     list.append(value)
# print(list)    



        #PROBLEM 2 👉 Separate integers and strings from a mixed list

# arr=[1, "a", 2, "b", 3]
# number=[]
# string=[]

# for i in arr:
#     if type(i)==int:
#         number.append(i)
#     else:
#         string.append(i)    

# print(number)  
# print(string)      



            #PROBLEM 3 Delete all occurrences of a given element from a list

# arr = [1,2,3,2,4,2]
# arr2=[]
# remove=2
# for i in arr:
#     if i!=remove:
#         arr2.append(i)
# print(arr2)


        #PROBLEM 4 👉 Find the second largest element in a list
# arr=[5, 3, 9, 9, 2]
# max=arr[0]
# smax=None    

# for i in arr:
#     if i > max :
#         smax=max
#         max=i
#     elif i < max and i > smax:
#         smax=i
    
# print(smax)    




        #PROBLEM 5 👉 Check if a list is palindrome
# arr=[1,8,3,3,8,0]
# start=0
# end=len(arr)-1
# is_palindrome=True
# for i in range(len(arr)//2):
#     if arr[start]!=arr[end]:
#         is_palindrome=False
#         break
#     else:
#         start=start+1
#         end=end-1
# print(is_palindrome)   




arr=[1,8,3,3,8,0]
start=0
end=len(arr)-1
is_palindrome=True
for i in range(len(arr)//2):
    if arr[start]!=arr[end]:
        is_palindrome=False
        break
    else:
        start=start+1
        end=end-1
print(is_palindrome) 