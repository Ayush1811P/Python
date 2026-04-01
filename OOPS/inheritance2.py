# class School:
#     def __init__(self,name,occupation):
#         self.name=name
#         self.occupation=occupation
#     def belongs_to(self):
#         return f"{self.name} belong to this school \n and he/she is {self.occupation} here"

# class student(School):
#     def belong_to(self):
#         return f"he is a student here"       
    
# class teacher(School):
#     ...


# person1=student("Ayush","Student")#1
# person2=teacher("Babbu","Teacher") #2       
# print(person1.belongs_to())#1(1)
# print("#"*30)
# print("/n",person1.belong_to())#1(2)
# print("*"*30)
# print(person2.belongs_to())#2(1)


class school:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def belongs_to(self):
        return f"{self.name} belong to this school \n and he/she is {self.occupation} here"

class student(school):
    ...

s1=student("ayush","Student")            