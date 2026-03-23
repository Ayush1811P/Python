# from abc import ABC , abstractclassmethod
# class Animal(ABC):
#     @abstractclassmethod
#     def speak(self):
#         pass
#     @abstractclassmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#     def move(self):
#         return "Running"
# d1=Dog()
#print(d1.speak(), d1.move())

from inheritance import bank_account , abstractmethod
class paytm(bank_account):
    @abstractmethod
    def show(self):
        return "Ture"
    

p1=paytm()
print(p1.show())