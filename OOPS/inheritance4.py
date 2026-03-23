        #PROGRAM 1

class vehicle:
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def describe(self):
        return f"I am {self.color} coloured {self.name}"    
class car(vehicle):
    def __init__(self,color,name,doors):
        super().__init__(color,name)
        self.doors=doors
    def appearances (self):
        parent_desc=super().describe()   
        return f"{parent_desc} with {self.doors} doors"
    
V1=vehicle("RED","LEMBORGINI")
#print(V1.describe())    

c1=car("BLUE","BMW",4)
# print(c1.appearances())


        #PROGRAM 1

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def appearance(self):
        return f"I am {self.name} {self.age} years old"            
    
class male(person):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender
    def display(self):
        parent_desc=super().appearance()
        return f"{parent_desc} {self.gender}"       

class female(person):
    def appearance(self):
        person_appearance=super().appearance()
        return f"{person_appearance} male"
         
m1=male("Ayush",23,"Male")    
print(m1.display())
p1=female("Babita",18)
print(p1.appearance())
