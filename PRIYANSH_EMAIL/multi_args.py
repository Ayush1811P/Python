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

# def mul(*nums):
#     mul=1
#     for i in nums:
#         mul*=i
#     return mul   

# print(mul(2,3,4,5) )   

"""                           a
func_name = keyword(lambda) lamda :  expressions a*a

                a  b 
func_name = lamda,lamda2:  
"""

# add=lambda a: a*a
# add2=lambda a: a+a+a+a
# print(add2(2))

add=lambda *a: [i*2 for i in a]
print(add(5,6,4,5))
#a=(2,4,5,3,9)