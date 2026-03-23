class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def voice(self):
        return f"i am {self.name} and my color is {self.color}"

class dog(Animal):
    def voice(self):
        return f"i am dog,{self.color} in color"        

class cat(Animal):
    ...

class cow(Animal):
    def __init__(self, name,color,nic_name):
           self.name=name
           self.color=color
           self.nic_name=nic_name
    def voice(self):
        print(f"\tMy nick name is: {self.nic_name}")
        return super().voice()  

A1=Animal("Snake","beggy")    #1
print("1: ",A1.voice())       #1(1)

D1=dog("Pattric","Golden")    #2
print("2: ",D1.voice())       #2(1)

c1=cat("KATEY","Brown")       #3
print("3: ",c1.voice())       #3(1)

cow1=cow("GAURI","White","GAU")    #4
print("4: ",cow1.voice())          #4(1)