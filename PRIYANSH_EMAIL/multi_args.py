import random
# def mul_add(*nums):#astric
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum

# print(mul_add())

# def details(course,*names):
#     print("COURSE IS: ",course)
#     for i in names:
#         print(i)

# details("BCA","Ayush","Priyansh","Ajay","Naman")

def mul(*nums):
    mul=1
    for i in nums:
        mul*=i
    return mul   

print(mul(2,3,4,5) )   