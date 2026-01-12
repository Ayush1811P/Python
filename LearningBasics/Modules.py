# import math
# print(math.sqrt(20))
# print(math.pow(2,2))
# print(math.floor(3.7))  #returns the left hand side value
# print(math.ceil(3.2))   #returns the next positive integer after float value
# print(math.factorial(5))
# print(math.pi)



        #RANDOM MODULE TO GET RANDOM VALUES

# import random
# print(random.random())  #return float random value
# print(random.randint(1,10))
# list=[10,45,3,52,5]
# print(random.choice(list))  #returns random value of list

# list2=[10,20,30,40,50]  #declared new list
# random.shuffle(list2)   #shuffling the list using random
# print(list2)

# print(random.sample(list2,3))#returns random 2 values from the list



        #METHOD 1
# import random
# OTP=[]
# for i in range(4):
#     OTP.append(random.randint(1,9))
# SIZE=len(OTP)
# Ostr=""
# for i in range(SIZE):
#         Ostr=Ostr + str(OTP[i])
# print(Ostr)        



        #METHOD 2
# import random
# OTP=random.randint(1000,9999)
# print(OTP)


        #METHOD 3

# import random
# OTP = random.sample(range(10),4)
# print(OTP)