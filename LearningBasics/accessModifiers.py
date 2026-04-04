# class test:
#     __name="Ayush"
#     __rollNo=18

#     def __showDetails(self):
#         name=self._test__name
#         rollno=self._test__rollNo
#         return f"{name},{rollno}"
    
# class test2(test):
#     ...
# t1=test()
# t1=test2()
# # t1._name="AAAYUSH"
# # print(t1.__name)        
# T1=test()
# print(T1._test__showDetails())





# class bank:
#     def __init__(self,username,password,balance):
#         self.username=username
#         self.__password=password
#         self.__balance=balance
#     def __show_credentials(self):
#         user=self.username
#         Passw=self.__password
#         bal=self.__balance
#         return f"{user}, {Passw},{bal}"
#     def show_bal(self):
#         return self.__balance
#     def __update_credentials(self,username,password,balance):
#         self.username=username
#         self.__password=password
#         self.__balance=balance
#     def add_balance(self):
#         bal=int(input("Enter balance to deposit: "))
#         self.__balance+=bal
#         return f"Updated balance is: {self.__balance}"
#     def widraw_money(self):
#         bal=int(input("Enter balance to widraw: "))
#         self.__balance=self.__balance-bal
#         return f"Updated balance is:{self.__balance}"
    
#-->Initializing a new object
#B1=bank("Ayush",8800,1000) 

#print(B1.show_bal()) #-->testing theshow balance method

#print(B1._bank__show_credentials()) 
#-->show all credentials is private (it is important data)
#hence it is privated 


#B1._bank__update_credentials("Ayush",1811,5000) 
#-> UPDATION OF WHOLE CREDENTIALS(VERY IMP TO HIDE )

#print(B1._bank__show_credentials())

#print(B1.add_balance())

#print(B1.widraw_money())

#print(B1._bank__show_credentials())







