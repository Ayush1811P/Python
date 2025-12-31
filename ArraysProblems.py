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



arr=[10,20,30,40,50,60]
n=len(arr)
mid=n//2
left=0
right =mid
result=[]
while left < mid and right< n:
    result.append(arr[left])
    result.append(arr[right])
    left=left+1
    right = right+1
    print(result)    