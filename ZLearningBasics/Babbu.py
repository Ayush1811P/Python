arr=[1,2,3,6,5,5,7,7,7,7,8,9,7,8]
arr2=[]
arr3 =[]
for y in range(len(arr)//2):
    arr2.append(arr[y])

for x in range (len(arr)//2,len(arr)):
    arr3.append(arr[x])
    


print(arr2)    
print(arr3)
