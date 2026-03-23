class paymentMethod:
    def pay(self,amount):
        pass
class credit_card(paymentMethod):
    def pay(self,amount):
        return f"Paid ${amount} using Credit Card"    
class PayPal(paymentMethod):
    def pay(self,amount):
        return f"Paid ${amount} using PayPal"   
class Paytm(paymentMethod):
    def pay(self,amount):
        return f"Paid ${amount} using Paytm"    
    


paytm=Paytm()
print(paytm.pay(2000))    
paypal=PayPal()
print(paypal.pay(1000))


class shape:
    def area(self):
        pass
    def parimeter(self):
        pass
class Square(shape):
    def __init__(self,side):
        self.side=side 
    def area(self):
        return  self.side*self.side
    def parimeter(self):
        return 4*self.side       
    
s1=Square()
   