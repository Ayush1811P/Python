# def greet(name,greeting="Hello"):
#     return f"{greeting} {name}"
# print(greet("Ayush"))



# def add_all(*nums):
#     total=0
#     for n in nums:
#         total=total+n
#     return total

# print(add_all(1,2,3,4,5)) 




# def show_info(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key}: {value}")


# print(show_info(name="ayush",age=20,city="Delhi"))

# info=show_info(name="ayush",age=20,city="Delhi")
# info2=show_info(name="Babbu",age=19,city="Delhi")        
# print(info,"\n",info2)






def double(n):   #1
    return n*2

def if_even(n):   #2
    if n%2==0:
        return True
    return False

def is_prime(n):  #3
    if n%2==0:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True

def square(n):
    result=n*n
    return result


def apply(numbers,operation):  #for single element
    result=operation(numbers)
    return result



def apply_all(nums,oper):    #for bunch of elements
    result=[]
    for n in nums:
        result.append(oper(n))
    return result    


#print(apply(8,double))
#print(apply_all([1,2,3,4,5],double))
#print(apply_all([1,2,3,4,5,6,7,8,9,10],if_even))
#print(apply(13,is_prime))
#print(apply_all([1,2,3,4,5],square))
print(apply(4,lambda x: x*2))