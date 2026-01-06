#print("hello")



# a =10
# b=10.5
# is_Empty = True

# print(type(a))
# print(type(b))
# print(type(is_Empty))


# name = input("YOUR NAME PLEASE:")
# print("Hello",name)


# age = -1
# if age >= 18:
#     print("You can drive")
# elif age < 0:
#     print("bakchodi mt kar")
# else:
#     print("balak h be tu")



#loops

# i=0
# while i <=5:
#     print("Serial number: ",i)
#     i+=1


# for i in range(1,6):
#     print("value: ",i)


# i=1
# while i != 7:
#     print("Value: ",i)
#     i=i+1



        #Function making and calling

# def add(a,b):
#     return a+b
# Result = add(10,20)
# print(Result)


        #ARRAY + ARRAYLIST

# number = [12,24,3,4,24,4]
# print(number)
# number.append(50) #to add a number in array on the last 
# print(number)
# number.remove(24)  # to remove element from array
# print(number)



# num = int(input("Enter number: "))
# if num == 0:
#     print("the number is zero")
# elif num < 0:
#     print("the number is negative")
# elif  num%2 ==0:
#     print("even")
# elif num%2 != 0:
#     print("ODD")
# else:
#     print("Invalid input")




# num = int(input("enter number:"))
# sum=0
# for i in range (1,num+1):
#     sum+=i
#     if i==num:
#         print("sum is: ",sum)


        #factorial code

# num = int(input("enter num: "))
# fact=1
# for i in range (1,num+1):
#     fact*=i
# print("the factorial is: ",fact)


        #REVERS A NUMBER
# num = int(input("Enter number: "))
# rev=0
# while num > 0:
#     rev= rev * 10 + num % 10
#     num//=10

# print("reversed =",rev)    



        # Fibonacci
# num = int(input("enter number: "))
# next=0
# for i in range(1,num+1):
#     print(next)
#     prev=i
#     next=prev + next



    #using SLICING  to reversea string
# string = input("enter your name:")
# reversed = string[::-1] ## string function to reverse string, list, touple
# print(reversed)


        ##CALCULATOR##

# num1= int(input("enter num1:"))
# operator = input("Enter operator: ")
# num2 = int(input("enter num2: "))

# match operator:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/":
#         if num2 != 0:
#             print(num1/num2)
#         else:
#             print("division not possible")

#     case "%":
#         print(num1%num2)
#     case "E":
#         exit        
            

    #LOGICAL, CONCEPTUAL AND FUNDAMENTAL OPERTION OF PYTHON
#a=10
#b = "10"
#c="hii"
#print(a,b)

#converting str into integer to perform operation usin -->int(b)<--
#print(int(b)+a)

#dose not change into integer instead use it as integer value to perform operations only
#print(int(b))

#to check dataType of variable
#print(type(b))

#repetition on a string with integer
#print(c * a)


        #LOGICAL DETAILS 
        #TRUE = 1,  FALSE =0
        #T + T MEANS 1 + 1
        #F + T ,MEANS 0 + 1
        # F + F MEANS 0+0


#print(True + True ) 
# print(False + True )
# print(False + False )


        #COMPARISON


#a=10 
#c="10"

#print(a == c)

#after conersion of str into integer
#print(a == int(c))


#DataType comparison
#print(a is c)

 

        #QUIZ FOR UH

        #Predict the output before running:

#print("5" * 2 + "3")  
#print(5 * 2 + int("3"))
#print(bool("False"))
#print(True * 10)
#print(bool())#if bol()is empty it will throw false


        ##KITNE SAHI THE?##
        #ASKING USER TO EXIT 
        #UNTILL KEEP EXECUTING A PROGRAM

# Exit=True
# while Exit ==True :
#     name=input("name:")
#     print("hello",name)
#     choice = int(input("want to exit yes =0 || No=1: "))
#     if choice ==0:
#         Exit=False
    

    #ARRAY TOPIC
 
#arr=[12,10.13,13123]
#arr1=["ayush",12,34.8,True,False]

    #array can hond any DataType

#print(arr[-1])#means print last element in the array
#print(arr1[-1])#means print last element in the array


        #TAKING USER INPUT 
# Array=[] 
# size = int(input("enter the size of array: "))
# for i in range(size):
#     #value =input("enter the element: ") this will take any type of value in array

#     value =int(input("enter the element: ")) #This will take onlyinteger as value
#     Array.append(value)


#Size = len(Array)#len acts as length.array means return the zise of the array


        #print only Even
# for i in range(Size):
#     if Array[i]%2==0:
#         print("Even number: ",Array[i])



        #initializing array dierectly with elements
#Array =[12,4,3,24,2,1,343,45,10]
#Size=len(Array)

#finding Max in the array
# max=Array[0]
# for i in range(Size):
#     if Array[i] > max:
#         max=Array[i]

# print(max)        

#mid = Array[Size//2]
#print(mid)


 