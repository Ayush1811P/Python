# arr=[10,20,30,40,50,60]
# result =[]
# n=len(arr)    
# mid=n//2
# left = mid - 1
# right = mid
# while left>=0 and right < n:
#     result.append(arr[left])
#     result.append(arr[right])
#     left = left-1
#     right=right+1

# print(result)

# arr=[10,20,30,1,40,50,60]
# min=arr[0]
# smin=min
# n=len(arr)
# for i in range (len(arr)):
#     if min > arr[i]:
#         smin=min
#         min = arr[i]
        
# print(min ,"and ", smin)




# arr=[10,20,30,40,50,60]
# sum=0
# for i in range(len(arr)):
#     sum=sum+arr[i]

# print(sum)



# arr=[10,20,30,40,50,60]
# n=len(arr)
# mid=n//2
# left=0
# right =mid
# result=[]
# while left < mid and right< n:
#     result.append(arr[left])
#     result.append(arr[right])
#     left= left+1
#     right = right+1
#     print(result)    








# arr=[10,20,30,40,50,60]
# result =[]
# n=len(arr)
# mid=n//2
# right=mid
# left=mid-1
# while left>=0 and right<n:
#     result.append(arr[right])
#     result.append(arr[left])
#     left= left-1
#     right= right+1
#     print(result)



    #Count & remove all zero elements
# arr=[0,34,0,45,0,56,0,46,0,67,0,76]
# n=len(arr)
# freq=0
# for i in range(n-1 , -1, -1):
#     if arr[i]== 0:
#         arr.pop(i)
#         freq= freq+1

# print(arr, " ",freq)        



#MOVE ZEROES TO THE END OF THE LIST

# arr=[0,34,0,45,0,56,0,46,0,67,0,76]
# n=len(arr)
# for i in range(n):
#     for j in range(n-1):
#         if arr[j]==0:
#             arr[j],arr[j + 1]= arr[j + 1],arr[j]
        
# print(arr)
# rev=[]
# for i in range(n-1,-1,-1):
#     rev.append(arr[i])

# print(rev)


# arr=[-1,0,4,-5,-3,53,-9,0,43,-11]
# positive=0
# negative=0
# zero=0
# for i in range(len(arr)):
#     if arr[i]<0:
#         negative=negative+1
#     elif arr[i]==0:
#         zero= zero+1
#     else:
#         positive=positive+1


# print("positive: ",positive,"Zero: ",zero," Negative: ",negative)        



# arr=[-1,0,4,-5,-3,53,-9,0,43,-11]
# rev=[]
# for i in range(len(arr)-1,-1,-1):
#     rev.append(arr[i])

# print(rev)    


# arr=[-1,0,4,-5,-3,53,-9,0,43,-11]
# arr2=[]
# for i in range(len(arr)):
#     arr2.append(arr[i])

# print(arr2)    


# arr=[-1,0,4,-5,-3,53,-9,0,43,-11]
# A=[]
# B=[]
# mid=len(arr)//2
# i=0
# while i<mid:
#     A.append(arr[i])
#     i=i+1

# for i in range(mid,len(arr)):
#     B.append(arr[i])

# print(A)    
# print(B)    


# arr=[10, 20, 30, 40, 50, 60]
# Result=[]
# n=len(arr)
# mid=n//2
# left=0
# right=mid

# while left < mid and right <=n:
#     Result.append(arr[left])
#     Result.append(arr[right])
#     left=left+1
#     right=right+1


# print(Result)


# arr=[10, 20, 30, 40, 50, 60]
# result=[]
# n=len(arr)
# mid=n//2
# left=mid-1
# right=mid
# while left>=0 and right <=n:
#     result.append(arr[left])
#     result.append(arr[right])
#     left=left-1
#     right = right+1

# print(result)




# arr=[0,1,0,3,0,5]       
# n=len(arr)
# for i in range(n):
#     for j in range(n-1):
#         if arr[j]==0:
#             arr[j + 1],arr[j]=arr[j],arr[j + 1] 

# print(arr)            


# arr=[1,2,3,9,1]
# n=len(arr)
# left=0
# right=len(arr)-1
# is_palindrome=True
# while left < right:
#     if arr[left] != arr[right]:
#         is_palindrome=False
#         break
#     left=left+1
#     right=right-1

# print(is_palindrome)


#arr=[12,34,1,45,45,1,34,12]
# i=0
# while i < len(arr):
#     j= i + 1
#     while j<len(arr):
#         if arr[i]==arr[j]:
#             arr.pop(j) 
#         else:
#             j +=1
#     i +=1
# print(arr)            

# arr = [10, 20, 30, 40, 50]
# arr2=[]
# k = 2
# for i in range(0,2):
#     arr2.append(arr[i]) 
# for i in range(0,2):
#     arr.pop(i)    

# print(arr2)
# print(arr)



# arr = [10, 20, 30, 40, 50]
# user_delete=int(input("Enter element to delete: "))
# user_enter=int(input("Enter element to replace: "))
# if user_delete==user_enter:
#     print("both are the same elements!")
# else:
#     for i in range(len(arr)):
#         if user_delete == arr[i]:
#             arr[i]=user_enter
#             print("Element Replaced successfully!")
#             break
#     else:
#         print("element not found!") 
         
# print(arr)        





#USING BINARY SEARCH TO REPLACE ELEMENT
# arr = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#     12, 14, 15, 18, 20, 21, 22, 24, 25, 27,
#     28, 30, 32, 33, 35, 36, 38, 40, 42, 44,
#     45, 47, 48, 50, 52, 54, 55, 57, 58, 60,
#     62, 63, 65, 66, 68, 70, 72, 74, 75, 77,
#     78, 80, 82, 84, 85, 87, 88, 90, 92, 94,
#     95, 97, 98, 100, 105, 110, 115, 120,
#     130, 140, 150, 160, 180, 200
# ]
# arr.sort()
# target=int(input("Enter the element to delete:"))
# replace=int(input("Enter the element to replace:"))
# if target==replace:
#     print("Both values are same!")
#     breakpoint
# else:   
#     start=0
#     end=len(arr)-1
#     while start <=end:
#         mid=(start + end)//2
#         if target==arr[mid]:
#             arr[mid]=replace
#             print("Element Replaced!")
#             break
#         elif target > arr[mid]:
#             start=mid+1       
#         else:       
#             end=mid-1   
#     print("element dose not exist!")
