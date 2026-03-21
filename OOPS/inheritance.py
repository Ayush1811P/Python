class bank_account:
    def __init__(self,user,balance):
        self.user=user
        self.__balance=balance #Encapsulation
    def details(self):
        return f"{self.user} your balance is {self.__balance}"    
                            #CLASS 1
class university(bank_account):#here i am just using the inheritance 
    ...#no line of code written yet giving output from prev class

class school(bank_account):#class 2 
    ...
# s1=school("Ayushi",190)
# print(s1.details())    
# s1.__balance=2000#this will not work because balance is encapsulated!
# print(s1.details())    

# b1=university("Ayush",1000)
# print(b1.details())

        