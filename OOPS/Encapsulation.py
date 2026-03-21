# class Bank_Account:
#     def __init__(self,user,balance):
#         self.user=user
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount >0:
#             self.__balance+=amount
#             return f"{amount} is added in your wallet."    
        
#         return -1
        
#     def widraw_money(self,amount):
#         if amount>0:
#             self.__balance-=amount
#             return f"{amount} deducted from your wallet."
        
#         return -1
#     def show_balance(self):
#         return f"{self.user} Your balance is: {self.__balance}"
    
# def main():
#     name=input("User name: ")
#     bal=int(input("Initial Balance: "))
#     acc1=Bank_Account(name,bal) 
#     print("1:Add Balance\t2:Widraw Amount\t3:show Balance\t 4:Exit")
#     while True:
#         Choice = int(input("Your choice: "))
#         match Choice:
#             case 1:
#                 bal=int(input("balance to add: "))
#                 acc1.deposit(bal)    
#             case 2:
#                 bal=int(input("balance to widraw: "))
#                 acc1.widraw_money(bal)               
#             case 3:
#                 print(acc1.show_balance())
                
#             case 4:
#                 return
                
# if __name__ == "__main__":
#     main()
              


class bank_account:
    def __init__(self,user,balance):
        self.user=user
        self.__balance=balance #Encapsulation
    def details(self):
        return f"{self.user} your balance is {self.__balance}"
    
b1=bank_account("Ayush",1000)
print(b1.details())
print(b1.user)    
print(b1.balance)    #cannot be accesible dierectly!