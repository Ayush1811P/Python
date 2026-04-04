class bank:
    def __init__(self,username,password,balance):
        self.username=username
        self.__password=password
        self.__balance=balance
    def __show_credentials(self):
        user=self.username
        Passw=self.__password
        bal=self.__balance
        return f"Name: {user}, \nPassword: {Passw},\nBalance:{bal}"
    def show_bal(self):
        return self.__balance
    def __update_credentials(self,username,password,balance):
        self.username=username
        self.__password=password
        self.__balance=balance
    def add_balance(self):
        bal=int(input("Enter balance to deposit: "))
        self.__balance+=bal
        return f"Updated balance is: {self.__balance}"
    def widraw_money(self):
        bal=int(input("Enter balance to widraw: "))
        self.__balance=self.__balance-bal
        return f"Updated balance is:{self.__balance}"




def create_account():   #ACCOUNT CREATION FUNCTION CALLING THE CLASS BANK
    credentials=False
    stop=False
    while stop ==False:
        user=input("Enter Name: ")
        name=user
        if user.isalpha():
            try:
                passw=int(input("Enter 6 digit password: "))
                if len(str(passw))<6:
                    credentials=False
                else:
                    credentials=True

                if credentials==True:

                    initial_bal=int(input("balance: "))
                    if not initial_bal:
                        credentials=False
                    else:
                        credentials=True
                        stop=True
            except ValueError:
                print(-1)             
        else:
            print("Enter valid name") 
    #print(user," ",passw," ",initial_bal)
    account =bank(user,passw,initial_bal)
    print("Account created!")
    #print(account._bank__show_credentials())
    return account

create_account() 

# def show_balance():
#     my_account=create_account()
#     return my_account.show_bal()
my_account=create_account()
print(my_account.show_bal())