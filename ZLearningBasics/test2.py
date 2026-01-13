# arr=[-1,3,-3,4,-4,5,0,0,-5,0,0]
# positive=0
# negative=0
# nutral=0
# try:
#     for i in arr:
#         if i<0:
#             negative+=1
#         elif i>0:
#             positive+=1
#         else:
#             nutral+=1  
# except ValueError:
#     print("error",False)

# print("Positives= ",positive, "Negative= ",negative,"Nutral= ",nutral)
  
    
    
arr=[10, 20, 30, 40, 50, 60]
result=[]
left=arr[0]
n=len(arr)
mid=len(arr)//2
right=mid
while left < mid and right < n:
    result.append(arr[left])
    result.append(arr[right])
    left+=1
    right+=1
print(arr)
print(result) 

