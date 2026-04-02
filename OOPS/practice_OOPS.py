class open_acc:
    def __init__(self,name,password):
        self.name=name
        self._password=password
    def created(self):
        return f"Account created with name {self.name}"
class add_balance:
    def __init__ (self,balance):
        self.balance=balance
    def balance_added(self):
        return f"Balance added {self.balance}"        
class bank_work(open_acc):
    def created(self):
        ...
class create_addbal(open_acc,add_balance):
    def __init__(self,name,password,balance):
        open_acc.__init__(self,name,password)
        add_balance.__init__(self,balance)
    def show(self):
        acc_msg=self.created()
        bal_msg=self.balance_added()
        return f"{acc_msg} and {bal_msg}"    

Account_open=open_acc("ayush",8800)
#print(Account_open.created())  
Bank_work=bank_work("Ayush",8800)
#print(Bank_work.created())  
create_add=create_addbal("Ayush",880081,41144)
print(create_add.show())