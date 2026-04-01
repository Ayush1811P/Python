# class paymentMethod:
#     def pay(self,amount):
#         pass
# class credit_card(paymentMethod):
#     def pay(self,amount):
#         return f"Paid ${amount} using Credit Card"    
# class PayPal(paymentMethod):
#     def pay(self,amount):
#         return f"Paid ${amount} using PayPal"   
# class Paytm(paymentMethod):
#     def pay(self,amount):
#         return f"Paid ${amount} using Paytm"    
    

class paymentMethod:
    def pay(self,amount):
        ...
        
class credit_card(paymentMethod):
    def pay(self, amount):
        return f"paid ${amount} using credit card!"
class PayPal(paymentMethod):
    def pay(self,amount):
        return f"Paid ${amount} using Paypal"
class Paytm(paymentMethod):
    def pay(self,amount):
        return f"Paid {amount} using Paytm"
    
paypal=PayPal()    
print(paypal.pay(3000))    
paytm = Paytm()
print(paytm.pay(2300))               
crd=credit_card()
print(crd.pay(4000))
# paytm=Paytm()
# print(paytm.pay(2000))    
# paypal=PayPal()
# print(paypal.pay(1000))


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
    
#s1=Square()
   