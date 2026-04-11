class Bank:
    def __init__(self,userName,initital_bal):
        self.userName=userName
        self.initial_bal = initial_bal
    def add_bal(self,balance):
        try:
            self.initial_bal+=balance
        except ValueError:
            print(-1)
        finally:
            print("curr Balance: ",self.initial_bal)    
    def widraw(self,balance):
        if balance>self.initial_bal:
            print("cannot procced due to low Balance")
        try:
            self.initial_bal-=balance
        except ValueError:
            -1
        finally:
            print("curr Balance: ",self.initial_bal)

# account=Bank("Ayush",1000)
# add=account.add_bal(2000)
# print(add)

a=12433
print(len(str(a)))